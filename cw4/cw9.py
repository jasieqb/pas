# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie UDP, dla pod-łączającego się klienta, odbierze od niego wiadomość o treści podanej w zadaniu nr 13 z laboratorium nr 3,a następnie odeśle klientowi odpowiedź TAK lub NIE. 
# W przypadku błędnego sformatowania wiadomości,serwer odeśle klientowi odpowiedź BADSYNTAX.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))

while True:
    try:
        data, addr = s.recvfrom(1024)
        print('Connection from', addr)

        data = data.decode('utf-8')
        data = data.split(' ')

        if len(data) != 3:
            s.sendto('BADSYNTAX'.encode('utf-8'), addr)
            continue

        data[0] = int(data[0])
        data[2] = int(data[2])
        if data[1] == '+':
            data = data[0] + data[2]
        elif data[1] == '-':
            data = data[0] - data[2]
        elif data[1] == '*':
            data = data[0] * data[2]
        elif data[1] == '/':
            data = data[0] / data[2]
        else:
            s.sendto('BADSYNTAX'.encode('utf-8'), addr)
            continue

        data = str(data).encode('utf-8')

        s.sendto(data, addr)
    except KeyboardInterrupt:
        s.close()
