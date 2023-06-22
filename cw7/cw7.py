# Napisz program klienta, który połączy się z wybranym serwerem POP3, a następnie wyświetli informacjęo tym, ile bajtów (w sumie) zajmują wiadomości znajdujące się w skrzynce

import socket

HOST = 'localhost'
PORT = 110

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'USER test\r\n')
    print(s.recv(1024).decode())
    
    s.sendall(b'PASS test\r\n')
    print(s.recv(1024).decode())
    
    s.sendall(b'STAT\r\n')
    
    response = s.recv(1024).decode()
    
    bajty = response.split(' ')[-1]
    
    print(f'Wiadomości zajmują {bajty} bajtów')
