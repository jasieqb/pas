# Napisz program klienta, który połączy się z serwerem TCP działającym pod adresem 212.182.24.27 naporcie 2900, a następnie będzie w pętli wysyłał do niego tekst wczytany od użytkownika, i odbierałodpowiedzi.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.25.252", 2900))
while True:
    msg = input("Message: ")
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())

s.close()
