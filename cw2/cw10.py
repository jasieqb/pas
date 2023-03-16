# Napisz program klienta, który połączy się z serwerem UDP działającym pod adresem 212.182.24.27 na
# porcie 2907, a następnie prześle do serwera nazwę hostname, i odbierze odpowiadający mu adres IP.

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.connect(("yuumi.skni.umcs.pl", 2907))
if soc:
    print("Połączono")

else:
    print("Nie połączono")
    exit()

soc.send(b"wp.pl")
print(soc.recv(1024))
