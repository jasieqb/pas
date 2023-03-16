# Napisz program klienta, który połączy się z serwerem UDP działającym pod adresem 212.182.24.27 naporcie 2902, a następnie prześle do serwera liczbę, operator, liczbę (pobrane od użytkownika) i odbierzeodpowiedź.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("212.182.25.252", 2902))
while True:
    msg = input("a: ")
    s.send(msg.encode())
    msg = input("znak: ")
    s.send(msg.encode())
    msg = input("b: ")
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())

s.close()
