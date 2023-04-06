# Napisz  program  serwera,  który  działając  pod  adresem  127.0.0.1  oraz  na  określonym  porcie  UDP,
# dla podłączającego się klienta, odbierze od niego nazwę hostname, i odeśle odpowiadający mu adres IP.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1239))

while True:
    try:
        data, addr = s.recvfrom(1024)
        print('Connection from', addr)
        s.sendto(socket.gethostbyname(data).encode(), addr)
    except KeyboardInterrupt:
        s.close()
