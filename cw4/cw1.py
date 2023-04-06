# Napisz  program  serwera,  który  działając  pod  adresem  127.0.0.1  oraz  na  określonym  porcie  TCP,
# dla
# podłączającego się klienta, będzie odsyłał mu aktualny czas oraz datę.
# Prawidłowa komunikacja powinnaodbywać się w nastepujacy sposób:
# •Serwer odbiera od klienta wiadomość (dowolną)
# •Serwer odsyła klientowi aktualną datę i czas

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)

while True:
    try:
        client, addr = s.accept()
        print('Connection from', addr)
        data = client.recv(1024)
        client.send(time.ctime().encode('utf-8'))
        client.send('\n'.encode('utf-8'))
        client.close()
    except KeyboardInterrupt:
        s.close()

s.close()
