# Napisz parę programów - klienta i serwer, w których porównasz czas przesyłu pakietów za pomocą gniazdaTCP i gniazda UDP. Następnie, po przeprowadzonym teście, odpowiedz na pytania:

import socket

# TCP server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)

while True:
    client, addr = s.accept()
    print(f'Connection from {addr}')
    client.send('Hello from server'.encode('utf-8'))
    client.close()
