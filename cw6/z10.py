# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP, będzieserwerem poczty, obsługującym protokół SMTP. Nie realizuj faktycznego wysyłania e-maila, tylko zasymuluj jego działanie tak, żeby napisany wcześniej klient SMTP myślał, że wiadomość została wysłana.Pamiętaj o obsłudze przypadku, gdy klient poda nie zaimplementowaną przez serwer komendę.

import socket


def handle_client(conn):
    conn.send(b'220 localhost SMTP ready\r\n')
    mail_from = None
    mail_to = []
    handshake = False
    while True:
        request = conn.recv(1024).decode('utf-8').strip()
        if not request:
            break

        if request.startswith('HELO') or request.startswith('EHLO'):
            conn.send(b'250 localhost\r\n')
            print(f'HELO {request[5:]}')
            handshake = True

        elif not handshake:
            conn.send(b'503 Bad sequence of commands\r\n')
            break

        elif request.startswith('MAIL FROM:') and handshake:
            conn.send(b'250 OK\r\n')
            print(f'MAIL FROM: {request[10:]}')
            mail_from = request[10:]

        elif request.startswith('RCPT TO:'):
            conn.send(b'250 OK\r\n')
            print(f'RCPT TO: {request[8:]}')
            mail_to.append(request[8:])
        elif request == 'DATA':
            print('DATA')
            conn.send(b'354 End data with <CR><LF>.<CR><LF>\r\n')
            data = ''
            while True:
                line = conn.recv(1024).decode('utf-8').strip()
                if line == '.':
                    break
                data += line + '\n'
            print(data)
            conn.send(b'250 OK\r\n')

        elif request == 'QUIT':
            conn.send(b'221 Bye\r\n')
            print('QUIT')
            break
        else:
            conn.send(b'502 Command not implemented\r\n')
            print(f'Unknown command: {request}')

    print(f'From: {mail_from}')
    print(f'To: {mail_to}')
    print(f'Data: {data}')
    print('Disconnected\r\n')


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 1587))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected by", addr)
    handle_client(conn)
    conn.close()
    # simple SMTP server
