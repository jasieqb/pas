# Napisz program klienta, który połączy się z serwerem IMAP, a następnie wyświetli informację o tym, ile  wiadomości znajduje się we wszystkich skrzynkach łącznie
import socket

HOST = 'localhost'
PORT = 143

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'LOGIN test test\r\n')
    s.recv(1024)
    print(s.recv(1024).decode())
    
    s.send(b'LIST "" *\r\n')
    mails = s.recv(1024).decode()
    
    count = 0
    
    mails = mails.split('\r\n')
    for mail in mails:
        if "EXISTS" in mail:
            print(mail)
            count += int(mail.split(' ')[1])
        
    print(f'Wszystkich maili jest {count}')
    
    s.send(b'LOGOUT\r\n')
    s.recv(1024)
    s.print(s.recv(1024).decode())
