# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie UDP,
#  dla podłączającego się klienta, odbierze od niego wiadomość o treści podanej w zadaniu nr 15 z laboratorium nr 3,
# a następnie odeśle klientowi odpowiedź TAK lub NIE. W przypadku błędnego sformatowania wiadomości,
# serwer odeśle klientowi odpowiedź BAD SYNTAX.

import socket


def checkA(mes: str) -> str:
    text = mes.split(';')
    print(text)
    if len(text) != 9:
        return 'BAD_SYNTAX1'
    if text[0] != 'zad15odpA':
        return 'BAD_SYNTAX2'
    if text[1] != 'ver':
        return 'BAD_SYNTAX3'
    if text[3] != 'srcip':
        return 'BAD_SYNTAX4'
    if text[5] != 'dstip':
        return 'BAD_SYNTAX5'
    if text[7] != 'type':
        return 'BAD_SYNTAX6'

    ver = int(text[2])
    scrip = text[4]
    dstip = text[6]
    typ = int(text[8])

    if ver == 4 and scrip == '212.182.24.27' and dstip == '192.168.0.2' and typ == 6:
        return 'TAK'
    else:
        return 'NIE'


def chcekB(mes: str) -> str:
    text = mes.split(';')
    if len(text) != 7:
        return 'BAD_SYNTAX'
    if text[0] != 'zad15odpB':
        return 'BAD_SYNTAX'
    if text[1] != 'srcport':
        return 'BAD_SYNTAX'
    if text[3] != 'dstport':
        return 'BAD_SYNTAX'
    if text[5] != 'data':
        return 'BAD_SYNTAX'

    scrport = int(text[2])
    dstport = int(text[4])
    data = text[6]

    if scrport == 2900 and dstport == 47526 and data == 'network programming is fun':
        return 'TAK'
    else:
        return 'NIE'


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 2911))

try:
    while True:
        data, addr = s.recvfrom(1024)
        print('Odebrano wiadomosc od', addr)
        print('Wiadomosc:', data)

        if data.startswith(b'zad15odpA'):
            s.sendto(checkA(data.decode('utf-8')).encode(), addr)
        elif data.startswith(b'zad15odpB'):
            s.sendto(chcekB(data.decode('utf-8')).encode(), addr)
        else:
            s.sendto('BAD_SYNTAX', addr)
finally:
    s.close()
