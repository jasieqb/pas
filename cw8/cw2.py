# Napisz program klienta, który połączy się z serwerem IMAP, a następnie wyświetli informację o tym, ilewiadomości znajduje się w skrzynceInbox.

import socket

HOST = 'localhost'
PORT = 143

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024).decode())
    s.send(b'LOGIN test test\r\n')
    s.recv(1024)
    print(s.recv(1024).decode())
    
    s.send(b'SELECT INBOX\r\n')
    s.recv(1024)
    print(s.recv(1024).decode())
    
    s.send(b'LIST "" INBOX\r\n')
    s.recv()
    print(s.recv(1024).decode())
    
    s.send(b'LOGOUT\r\n')
    s.recv(1024)
    
    print(s.recv(1024).decode())
    
    
    
