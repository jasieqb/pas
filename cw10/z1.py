# Napisz program klienta, który nawiąże połączenie (handshake) z serwerem obsługującym protokół We-bSocket, działającym pod adresemws://echo.websocket.orgna porcie 80.

import socket
import struct


SERVER = "localhost"
PORT = 8080

ENDPOINT = "/.ws"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

handshake = "GET " + ENDPOINT + " HTTP/1.1\r\n" + \
            "Host: " + SERVER + "\r\n" + \
            "Upgrade: websocket\r\n" + \
            "Connection: Upgrade\r\n" + \
            "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n" + \
            "Sec-WebSocket-Version: 13\r\n " + \
            "\r\n\r\n"

s.send(handshake.encode())

response = s.recv(1024)
print(response.decode())

s.close()
