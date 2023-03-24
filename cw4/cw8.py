# Zmodyfikuj program nr 7 z laboratorium nr 3 w ten sposób, aby mieć pewność,
# że serwer w rzeczywistościodebrał / wysłał wiadomość o wymaganej długości.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))

while True:
    try:
        data, addr = s.recvfrom(20)
        print('Connection from', addr)
        print('Data:', data)
        send = s.sendto(data, addr)
        while send != len(data):
            send += s.sendto(data[send:], addr)
    except KeyboardInterrupt:
        s.close()
