# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP, będzieserwerem poczty, obsługującym protokół IMAP. Nie realizuj faktycznego pobierania e-maili, tylko zasymu-luj jego działanie tak, żeby napisany wcześniej klient IMAP mógł pobrac wiadomosci. Pamiętaj o obsłudzeprzypadku, gdy klient poda nie zaimplementowaną przez serwer komendę.

import socket

# Sample email data to be returned by the server
EMAILS_DATA = [[b'Subject: Test email\r\n',        b'From: sender@example.com\r\n',        b'To: recipient@example.com\r\n',        b'\r\n',        b'This is a test email.\r\n'],
               [b'Subject: Hello World\r\n',        b'From: john@example.com\r\n',        b'To: jane@example.com\r\n',        b'\r\n',
                   b'Hello Jane,\r\n\r\nJust wanted to say hello and see how you\'re doing.\r\n\r\nBest regards,\r\nJohn\r\n'],
               [b'Subject: Project Update\r\n',        b'From: sarah@example.com\r\n',        b'To: mike@example.com\r\n',        b'\r\n',
                   b'Hi Mike,\r\n\r\nI wanted to give you a quick update on the project we\'ve been working on.\r\n\r\nWe\'ve made significant progress over the past week and are on track to complete the project on time. I\'ll be sending a detailed report to you and the rest of the team later today.\r\n\r\nLet me know if you have any questions or concerns.\r\n\r\nBest regards,\r\nSarah\r\n']
               ]


def handle_client(conn):
    conn.send(b'* OK IMAP4rev1 Service Ready\r\n')
    username = None
    auth = False
    while True:
        request = conn.recv(1024).decode('utf-8').strip()
        if not request:
            break

        if request.startswith('LOGIN '):
            username, password = request[6:].split(' ')
            if username == 'test' and password == 'test':
                conn.send(b'* OK Logged in\r\n')
                auth = True
            else:
                conn.send(b'* NO Invalid username or password\r\n')

        elif request == 'LIST "" *' and auth:
            num_emails = len(EMAILS_DATA)
            response = '* LIST () "." "INBOX"\r\n'
            for i, email in enumerate(EMAILS_DATA, start=1):
                response += f'* {i} EXISTS\r\n'
                response += f'* {i} RECENT\r\n'
            response += '* OK Completed (Success)\r\n'
            conn.send(response.encode())

        elif request.startswith('FETCH ') and auth:
            email_num = int(request.split(' ')[1])
            if email_num <= 0 or email_num > len(EMAILS_DATA):
                conn.send(b'* NO Invalid email number\r\n')
            else:
                email = EMAILS_DATA[email_num - 1]
                response = f'* {email_num} FETCH (BODY[HEADER] {{10}}\r\n'
                response += b''.join(email).decode()
                response += b')\r\n'
                conn.send(response.encode())

        elif request == 'LOGOUT':
            conn.send(b'* BYE IMAP4rev1 Server logging out\r\n')
            break

        else:
            conn.send(b'* BAD Command not recognized\r\n')

    conn.close()


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 143))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected by", addr)
    handle_client(conn)
