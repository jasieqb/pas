# Napisz program klienta, który nawiąże połączenie (handshake) z serwerem obsługującym protokół We-bSocket, działającym pod adresemws://echo.websocket.orgna porcie 80.

import socket
import struct

import os


def random_key():
    return os.urandom(4)


def prepare_frame(message):
    frame = bytearray()
    frame.append(0x81)
    if (len(message) <= 125):
        frame.append(len(message) + 128)
    key = random_key()
    frame.extend(key)

    message_bytes = message.encode('utf-8')

    for i in range(len(message)):
        frame.append(message_bytes[i] ^ key[i % 4])
    return frame


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
print(s.recv(1024))
mess = "Hello, server!"

frame = prepare_frame(mess)
s.send(frame)


response = s.recv(1024)
print(response)

s.close()
