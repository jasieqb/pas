# Napisz  program  serwera,  który  działając  pod  adresem  127.0.0.1  oraz  na  określonym  porcie  UDP,
# dla podłączającego się klienta, odbierze od niego adres IP,
# i odeśle odpowiadającą mu nazwę hostname.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1238))

while True:
    try:
        data, addr = s.recvfrom(1024)
        print('Connection from', addr)
        print('Data:', data)
        s.sendto(socket.gethostbyaddr(data)[0].encode(), addr)
    except KeyboardInterrupt:
        s.close()
