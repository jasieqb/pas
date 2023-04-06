# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie UDP, dla pod-łączającego się klienta, odbierze od niego wiadomość o treści podanej w zadaniu nr 13 z laboratorium nr 3,a następnie odeśle klientowi odpowiedź TAK lub NIE.
# W przypadku błędnego sformatowania wiadomości,serwer odeśle klientowi odpowiedź BAD_SYNTAX.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 2910))

try:
    while True:
        data, addr = s.recvfrom(1024)
        print('Odebrano wiadomosc od', addr)
        print('Wiadomosc:', data)
        data = data.decode('utf-8')
        tmp = data.split(';')
        if len(tmp) != 7:
            s.sendto(b'BAD_SYNTAX', addr)
            continue

        if tmp[0] != 'zad14odp':
            s.sendto(b'BAD_SYNTAX', addr)
            continue

        if tmp[1] != 'src':
            s.sendto(b'BAD_SYNTAX', addr)
            continue

        if tmp[3] != 'dst':
            s.sendto(b'BAD_SYNTAX', addr)
            continue

        if tmp[5] != 'data':
            s.sendto(b'BAD_SYNTAX', addr)
            continue

        if data == 'zad14odp;src;60788;dst;2901;data;programming in python is fun':
            s.sendto(b'TAK', addr)
        else:
            s.sendto(b'NIE', addr)
finally:
    s.close()
