# Napisz parę programów - klienta i serwer, w których porównasz czas przesyłu pakietów za pomocą gniazdaTCP i gniazda UDP. Następnie, po przeprowadzonym teście, odpowiedz na pytania:

# UDP server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1235))

while True:
    data, addr = s.recvfrom(1024)
    print(f'Connection from {addr}')
    s.sendto('Hello from server'.encode('utf-8'), addr)

addr.close()
