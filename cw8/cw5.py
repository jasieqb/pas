# Napisz program klienta, który połączy się z serwerem IMAP, a następnie ﬁzycznie usunie wybraną wiadomość
import socket

HOST = 'localhost'
PORT = 143

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024).decode())
    s.send(b'A1 LOGIN test test\r\n')
    s.recv(1024)
    print(s.recv(1024).decode())
    
    s.send(b'A1 SELECT INBOX\r\n')
    s.recv(1024)
    print(s.recv(1024).decode())
    
    # usuniecie wiadomosci
    s.send(b'A1 STORE 1 +FLAGS \Deleted')
    s.send(b'A2 EXPUNGE')
