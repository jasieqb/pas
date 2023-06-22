# Napisz program klienta, który połączy się z serwerem IMAP, a następnie sprawdzi, czy w skrzynce są nieprzeczytane wiadomości. Jeśli tak, wyświetli treść wszystkich nieprzeczytanych wiadomości oraz oznaczy je jako przeczytane (komenda STORE i flagi - FLAGS).
import socket

HOST = 'localhost'
PORT = 143

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.send(b'A1 LOGIN test test\r\n')
    s.recv(1024)
    print(s.recv(1024).decode())
    
    s.send(b'A1 SELECT INBOX\r\n')
    s.recv(1024)
    s.print(s.recv(1024).decode())
    
    # select unread messages
    s.send(b'A1 SEARCH NEW\r\n')
    data = s.recv(1024).decode().strip()
    
    mails = data.split(' ')[2:]
    
    for mail in mails:
        s.send(f'A1 FETCH {mail} BODY[TEXT]\r\n'.encode())
        print(s.recv(1024).decode())
        
        s.send(f'A1 STORE {mail} FLAGS (\Seen)\r\n'.encode())
        print(s.recv(1024).decode())
        
    s.send(b'A1 LOGOUT\r\n')
    
    
    
