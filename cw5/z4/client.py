# Napisz parę programów - klienta i serwer, w których porównasz czas przesyłu pakietów za pomocą gniazdaTCP i gniazda UDP. Następnie, po przeprowadzonym teście, odpowiedz na pytania:
# client
import socket
import time

# TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start = time.time()
s.connect(('localhost', 1234))
s.send('Hello from client'.encode('utf-8'))
data = s.recv(1024)
end = time.time()
print(f'TCP: {end - start}')
s.close()

# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start = time.time()
s.connect(('localhost', 1235))
s.send('Hello from client'.encode('utf-8'))
data = s.recv(1024)
end = time.time()
print(f'UDP: {end - start}')
s.close()
