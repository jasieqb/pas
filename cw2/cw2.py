# Napisz program klienta, który połączy się z serwerem TCP działającym pod adresem 212.182.24.27 naporcie 2900, a następnie wyśle do niego wiadomość i odbierze odpowiedź.
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.25.252", 2900))
s.send(b"Hello, server!")
data = s.recv(1024)
s.close()
print(data)
