# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP, będzieserwerem poczty, obsługującym protokół POP3. Nie realizuj faktycznego pobierania e-maili, tylko zasymu-luj jego działanie tak, żeby napisany wcześniej klient POP3 mógł pobrac wiadomosci. Pamiętaj o obsłudzeprzypadku, gdy klient poda nie zaimplementowaną przez serwer komendę.

import socket

# Sample email data to be returned by the server
EMAILS_DATA = [
    [
        b'Subject: Test email\r\n',
        b'From: sender@example.com\r\n',
        b'To: recipient@example.com\r\n',
        b'\r\n',
        b'This is a test email.\r\n'
    ],
    [
        b'Subject: Hello World\r\n',
        b'From: john@example.com\r\n',
        b'To: jane@example.com\r\n',
        b'\r\n',
        b'Hello Jane,\r\n\r\nJust wanted to say hello and see how you\'re doing.\r\n\r\nBest regards,\r\nJohn\r\n'
    ],
    [
        b'Subject: Project Update\r\n',
        b'From: sarah@example.com\r\n',
        b'To: mike@example.com\r\n',
        b'\r\n',
        b'Hi Mike,\r\n\r\nI wanted to give you a quick update on the project we\'ve been working on.\r\n\r\nWe\'ve made significant progress over the past week and are on track to complete the project on time. I\'ll be sending a detailed report to you and the rest of the team later today.\r\n\r\nLet me know if you have any questions or concerns.\r\n\r\nBest regards,\r\nSarah\r\n' + \
        b'--boundary_123456789 \r\n' + \
        b'Content-Type: image/jpeg \r\n' + \
        b'Content-Disposition: attachment; filename="example.jpg" \r\n' + \
        b'Content-Transfer-Encoding: base64 \r\n\r\n' + \
        b'/9j/4AAQSkZJRgABAQEAAAAAAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCABkAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmpqeoqaaKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT'
        
    ]
    
]


def handle_client(conn):
    conn.send(b'+OK POP3 server ready\r\n')
    username = None
    password = None
    auth = False
    while True:
        request = conn.recv(1024).decode('utf-8').strip()
        if not request:
            break

        if request.startswith('USER '):
            username = request[5:]
            conn.send(b'+OK\r\n')

        elif request.startswith('PASS '):
            password = request[5:]
            if username == 'test' and password == 'test':
                conn.send(b'+OK Logged in\r\n')
                auth = True
            else:
                conn.send(b'-ERR Invalid username or password\r\n')

        elif request == 'STAT' and auth:
            num_emails = len(EMAILS_DATA)
            total_size = sum(len(email) for email in EMAILS_DATA)
            conn.send(f'+OK {num_emails} {total_size}\r\n'.encode())

        elif request == 'LIST' and auth:
            num_emails = len(EMAILS_DATA)
            response = '+OK\r\n'
            for i, email in enumerate(EMAILS_DATA, start=1):
                response += f'{i} {len(email)}\r\n'
            response += '.\r\n'
            conn.send(response.encode())

        elif request.startswith('RETR ') and auth:
            email_num = int(request[5:])
            if email_num <= 0 or email_num > len(EMAILS_DATA):
                conn.send(b'-ERR Invalid email number\r\n')
            else:
                email = EMAILS_DATA[email_num - 1]
                response = f'+OK {len(email)} octets\r\n'
                for line in email:
                    response += line.decode()
                response += '.\r\n'
                conn.send(response.encode())

        elif request.startswith('DELE ') and auth:
            email_num = int(request[5:])
            if email_num <= 0 or email_num > len(EMAILS_DATA):
                conn.send(b'-ERR Invalid email number\r\n')
            else:
                conn.send(b'+OK\r\n')
        
        elif request == 'QUIT':
            conn.send(b'+OK Bye\r\n')
            break

        else:
            conn.send(b'-ERR Command not recognized\r\n')
            
        

    conn.close()


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1102))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected by", addr)
    handle_client(conn)
