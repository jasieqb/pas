# Napisz program klienta, który połączy się z serwerem UDP działającym pod adresem 212.182.24.27 naporcie 2901, a następnie wyśle do niego wiadomość i odbierze odpowiedź.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("212.182.25.252", 2901))
s.send(b"Hello, server!")
data = s.recv(1024)
s.close()
print(data)
