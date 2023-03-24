# Zmodyfikuj program nr 2 z laboratorium nr 3 w ten sposób, aby serwer wysyłał i co
# dbierał wiadomość o maksymalnej długości 20 znaków.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))

while True:
    try:
        data, addr = s.recvfrom(20)
        print('Connection from', addr)
        print('Data:', data)
        s.sendto(data, addr)
    except KeyboardInterrupt:
        s.close()

