# Napisz program klienta, który połączy się z serwerem UDP działającym pod adresem 212.182.24.27 na
# porcie 2906, a następnie prześle do serwera adres IP, i odbierze odpowiadającą mu nazwę hostname.


import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.connect(("212.182.25.252", 2906))
if soc:
    print("Połączono")

else:
    print("Nie połączono")
    exit()

soc.send(b"212.182.25.252")
print(soc.recv(1024))
