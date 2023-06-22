# Napisz program klienta, który połączy się z wybranym serwerem POP3, a następnie pobierze z serwerawiadomość z załącznikiem (obrazkiem) i zapisze obrazek na dysk. Nazwa obrazka musi zgadzać się z nazwązałącznika podaną w mailu. Pamiętaj, że do przesyłania załączników binarnych w poczcie elektronicznejwykorzystywane jest kodowanieBase64

import socket
import base64

HOST = 'localhost'
PORT = 1102

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'USER test\r\n')
    print(s.recv(1024).decode())
    
    s.sendall(b'PASS test\r\n')
    print(s.recv(1024).decode())
    
    # get 3 message with attachment
    
    s.sendall(b'RETR 3\r\n')
    response = s.recv(1024).decode()
    
    atachment = response.split('\r\n\r\n')[-1]
    
    # # remove dot and \r\n
    # print(atachment_with_dot)
    
    # atachment = atachment_with_dot[:-3]
    print(atachment)
    
    with open('obrazek.png', 'wb') as f:
        f.write(base64.b64decode(atachment))
        
    print('END')
    
