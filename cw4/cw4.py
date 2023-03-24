# Napisz  program  serwera,  który  działając  pod  adresem  127.0.0.1  oraz  na  określonym  porcie  UDP,
# dla podłączającego się klienta, będzie odbierał liczbę, operator i liczbę,
# a następnie odsyłał użytkownikowiwynik działania, przez niego przesłanego.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))

while True:
    try:
        data, addr = s.recvfrom(1024)
        print('Connection from', addr)

        data = data.decode('utf-8')
        try:
            data = int(data)
        except ValueError:
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
            data = 'Wrong operator'

        data = str(data).encode('utf-8')

        s.sendto(data, addr)
    except KeyboardInterrupt:
        s.close()

s.close()
