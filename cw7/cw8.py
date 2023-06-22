# Napisz program klienta, który połączy się z wybranym serwerem POP3, a następnie wyświetli informacjęo tym, ile bajtów zajmuje każda wiadomość (z osobna) znajdująca się w skrzynce.

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
    
    for line in response.split('\r\n')[1:-2]:
        print(line.split(' ')[-1])

    