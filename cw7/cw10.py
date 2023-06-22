# Napisz program klienta, który połączy się z wybranym serwerem POP3, a następnie wyświetli wszystkiewiadomości znajdujące się w skrzynce.

import socket

HOST = 'localhost'
PORT = 110

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'USER test\r\n')
    print(s.recv(1024).decode())
    
    s.sendall(b'PASS test\r\n')
    print(s.recv(1024).decode())
    
    s.sendall(b'LIST\r\n')
    
    lista = s.recv(1024).decode()
    
    lista = lista.split('\r\n')[1:-1]
    lista = [int(x.split(' ')[0]) for x in lista]
    
    for i in lista:
        s.sendall(f'RETR {i}\r\n'.encode())
        print(s.recv(1024).decode())
        
        print('-----------------------------------')
        
    print('END')
