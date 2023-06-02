# Simple irc client with weather api

import socket
import ssl
import sys
import time
import re
import json

ERROR = -1
SUCCESS = 0


class SimpleWeatherApi:

    def __init__(self, api_key):
        self.api_key = api_key

    def _format_mess(self, body) -> str:
        formatted_data = f"Weather in {body['name']}: {body['weather'][0]['description']}\n"
        formatted_data += f"Temperature: {body['main']['temp']} K\n"
        formatted_data += f"Feels like: {body['main']['feels_like']} K\n"
        formatted_data += f"Humidity: {body['main']['humidity']}%\n"
        formatted_data += f"Wind speed: {body['wind']['speed']} m/s\n"
        formatted_data += f"Cloudiness: {body['clouds']['all']}%\n"

        return formatted_data

    def get_weather(self, city):
        soc1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc1.connect(("api.openweathermap.org", 443), )
        soc1 = ssl.wrap_socket(soc1, ssl_version=ssl.PROTOCOL_TLSv1_2,
                               cert_reqs=ssl.CERT_NONE)

        # get location
        # print(self.api_key)
        soc1.sendall(
            # f'GET /geo/1.0/direct?q={city}&appid={self.api_key} HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n'.encode("utf-8"))
            f'GET /geo/1.0/direct?q={city}&appid={self.api_key} HTTP/1.1\r\nHost: api.openweathermap.org\r\nAccept: */*\r\n\r\n'.encode("utf-8"))

        data = soc1.recv(4096)
        soc1.close()
        print(data)
        body = data.decode("utf-8").split("\r\n\r\n")[1]
        # print(body)
        try:
            lat = json.loads(body)[0].get("lat")
            lon = json.loads(body)[0].get("lon")
        except:
            return ERROR, "City not found"

        # print(lat, lon)

        soc2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc2.connect(("api.openweathermap.org", 443), )
        soc2 = ssl.wrap_socket(soc2, ssl_version=ssl.PROTOCOL_TLSv1_2,
                               cert_reqs=ssl.CERT_NONE)

        soc2.sendall(
            f"GET /data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key} HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n".encode("utf-8"))

        data = soc2.recv(4096)
        soc2.close()
        body = data.decode("utf-8").split("\r\n\r\n")[1]
        try:
            body = json.loads(body)
        except:
            return ERROR, "Not found"
        # print(body)
        body = self._format_mess(body)
        return SUCCESS, body
    # print(body)


class IrcClient:

    def __init__(self, host, port, nick, user, realname, channel, api_key):
        self.host = host
        self.port = port
        self.nick = nick
        self.user = user
        self.realname = realname
        self.channel = channel
        # self.api_key = api_key
        self.cli = SimpleWeatherApi(api_key)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port), )

        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = True
        self.ctx.verify_mode = ssl.CERT_REQUIRED
        self.ctx.load_verify_locations("ca.pem")
        # self.ctx.protocol = ssl.PROTOCOL_TLSv1_2
        # self.ctx.load_default_certs()

        self.s = self.ctx.wrap_socket(
            self.s, server_hostname=self.host)
        # self.s = ssl.wrap_socket(self.s, server_hostname=self.host,)
        #  cert_reqs=ssl.CERT_NONE)

        cert = self.s.getpeercert()
        print(cert["issuer"])
        if not cert or ssl.match_hostname(cert, self.host):
            raise Exception("Invalid certificate")
        # if not cert["issuer"] == cert["subject"]:
            # raise Exception("Invalid certificate")

        ### INIT MESSAGES ###
        self.sendall(("NICK %s\r\n" % self.nick).encode("utf-8"))
        self.sendall(("USER %s %s %s :%s\r\n" % (self.user, self.user,
                                                 self.user, self.realname)).encode("utf-8"))
        self.sendall(("JOIN %s\r\n" % self.channel).encode("utf-8"))

        # self.weather = self.cli.get_weather("London")

    def sendall(self, message: bytes):
        print(f'> {message}')
        self.s.sendall(message)

    def send(self, message):
        print(f'> {message}')
        self.s.sendall(message.encode("utf-8"))

    def recv(self):
        data = self.s.recv(1024)
        print(f'< {data}')
        return data.decode("utf-8")

    def close(self):
        self.s.close()

    def send_message(self, mess):
        self.send(f"PRIVMSG {self.channel} :{mess}\r\n")

    def get_weather(self, city):
        """
        Get weather from openweather api
        """

        return self.cli.get_weather(city)

    def handle_message(self, mess):
        if mess.startswith("!hello"):
            self.send_message("Hello!")

        if mess.startswith("!quit"):
            self.send_message("Bye!")
            self.send("QUIT\r\n")
            self.close()
            sys.exit(0)

        if mess.startswith("!help"):
            self.send_message("Commands: !hello, !quit, !help\r\n")

        if mess.startswith("!weather"):
            city = mess.split(" ")[1].strip()
            # print(city.strip())
            status, mess = self.cli.get_weather(city)

            if status == SUCCESS:
                for mess in mess.split("\n"):
                    print(mess)
                    self.send_message(mess)
                # self.send_message(mess)
            elif status == ERROR:
                self.send_message("ERROR during fetching data")

    def run(self):
        while True:
            data = self.recv()
            # print(data)

            if data.startswith("PING"):
                ping = data.split("PING :")[1]
                self.send(f"PONG {ping}\r\n")

            if re.search(f"PRIVMSG {self.channel} :.+", data):
                mess = re.split(f"PRIVMSG {self.channel} *:", data)[1]
                self.handle_message(mess)
                # print(mess)
                # self.send(
                # f"PRIVMSG {self.channel} :Hello!, your mess is */: {mess}\r\n")

            if "JOIN" in data and "not registered" in data.lower():
                # print("JOIN", data)
                # self.send("PRIVMSG #test :Hello!\r\n"
                self.sendall(("JOIN %s\r\n" % self.channel).encode("utf-8"))

            time.sleep(1)


def main():
    client = IrcClient("chat.freenode.net", 7000, "testbot1", "testbot1",
                       "testbot1", "#test123", "d4af3e33095b8c43f1a6815954face64")
    client.run()
    # cli_we = SimpleWeatherApi("d4af3e33095b8c43f1a6815954face64")
    # print(cli_we.get_weather("London"))


if __name__ == "__main__":
    main()
