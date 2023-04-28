# Napisz program klienta, który połączy się z serwerem IMAP, a następnie wyświetli informację o tym, ilewiadomości znajduje się w skrzynceInbox.

import socket

HOST = 'localhost'
PORT = 110

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024).decode())
    s.send(b'USER test\r\n')
    print(s.recv(1024).decode())
    s.send(b'PASS test\r\n')
    print(s.recv(1024).decode())
    s.send(b'STAT\r\n')
    print(s.recv(1024).decode())
    s.send(b'LIST\r\n')
    print(s.recv(1024).decode())
    s.send(b'RETR 1\r\n')
    print(s.recv(1024).decode())
    s.send(b'QUIT\r\n')
    print(s.recv(1024).decode())
