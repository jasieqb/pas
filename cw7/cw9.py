# Napisz program klienta, który połączy się z wybranym serwerem POP3, a następnie wyświetl treść wia-domości o największym rozmiarze.

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
    
    
    response = s.recv(1024).decode()
    
    
    # find the biggest message
    num = -1
    size = -1
    for line in response.split('\r\n')[1:-1]:
        if int(line.split(' ')[-1]) > size:
            num = int(line.split(' ')[0])
            size = int(line.split(' ')[-1])
        
    # get the message
    s.sendall(f'RETR {num}\r\n'.encode())
    print(s.recv(1024).decode())
        
