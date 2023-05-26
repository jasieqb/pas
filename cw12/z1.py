# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP będzieserwerem echa, który będzie odsyłał podłączającym się klientom odebrane od nich wiadomości.

import socket
import datetime

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

    def __str__(self):
        return f'{self.host}:{self.port}'

    def __repr__(self):
        return f'{self.host}:{self.port}'

    def accept(self):
        try:
            conn, addr = self.server_soc.accept()
            self.clients.append(Client(conn, addr))
            with open('log.txt', 'a') as f:
                print(f'New client: {addr}', file=f)
        except BlockingIOError:
            pass

    def recv(self):
        for client in self.clients:
            try:
                data = client.conn.recv(1024)
                if data:
                    client.data += data
                else:
                    with open('log.txt', 'a') as f:
                        print(
                            f'Client {client.addr} disconnected', file=f)
                    self.clients.remove(client)
            except BlockingIOError:
                pass

    def send(self):
        for client in self.clients:
            if client.data:
                try:
                    client.conn.sendall(client.data)
                    client.data = b''
                except BlockingIOError:
                    pass

    def run(self):
        with open('log.txt', 'a') as f:
            print(f'Server started at {self}', file=f)
        while True:
            self.accept()
            self.recv()
            self.send()


if __name__ == '__main__':
    server = Server(HOST, PORT)
    server.run()
