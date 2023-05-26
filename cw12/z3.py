# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP będzielosował liczbę i odbierał od klienta wiadomości. W przypadku, gdy w wiadomości klient przyśle do serweracoś innego, niż liczbę, serwer powinien poinformować klienta o błędzie. Po odebraniu liczby od klienta,serwer sprawdza, czy otrzymana liczba jest:
# •mniejsza od wylosowanej przez serwer
# •równa wylosowanej przez serwer
# •większa od wylosowanej przez serwerA następnie odsyła stosowną informację do klienta. W przypadku, gdy klient odgadnie liczbę, klientpowinien zakończyć działanie.

import socket
import random

HOST = '127.0.0.1'
PORT = 6543


class Client():
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.conn.setblocking(False)
        self.data = b''

    def __str__(self):
        return str(self.addr)

    def __repr__(self):
        return str(self.addr)


class Server():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.bind((self.host, self.port))
        self.server_soc.setblocking(False)
        self.server_soc.listen(5)
        self.number = random.randint(0, 100)
        print(f'Number: {self.number}')

    def __str__(self):
        return f'{self.host}:{self.port}'

    def __repr__(self):
        return f'{self.host}:{self.port}'

    def accept(self):
        try:
            conn, addr = self.server_soc.accept()
            self.clients.append(Client(conn, addr))
            print(f'New client: {addr}')
        except BlockingIOError:
            pass

    def recv(self):
        for client in self.clients:
            try:
                data = client.conn.recv(1024)
                if data:
                    client.data += data
                else:
                    print(f'Client {client.addr} disconnected')
                    self.clients.remove(client)
            except BlockingIOError:
                pass

    def send(self):
        for client in self.clients:
            if client.data:
                try:
                    number = int(client.data.decode())
                    if number < self.number:
                        client.conn.send(b'Less\n')
                    elif number > self.number:
                        client.conn.send(b'More\n')
                    else:
                        client.conn.send(b'You win!\n')
                        self.clients.remove(client)
                except ValueError:
                    client.conn.send(b'Not a number\ns')
                client.data = b''

    def run(self):
        while True:
            self.accept()
            self.recv()
            self.send()


if __name__ == '__main__':
    server = Server(HOST, PORT)
    server.run()
