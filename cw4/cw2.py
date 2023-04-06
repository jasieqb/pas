# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP,
# dla podłą-czającego się klienta, będzie odsyłał mu przesłaną wiadomość (tzw. serwer echa).
#  Prawidłowa komunikacjapowinna odbywać się w nastepujacy sposób:
# •Serwer odbiera dane od klienta
# •Serwer odsyła klientowi odebrane od niego dane

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1235))
s.listen(5)

while True:
    try:
        client, addr = s.accept()
        print('Connection from', addr)
        data = client.recv(1024)
        client.send(data)
        client.close()
    except KeyboardInterrupt:
        s.close()

s.close()
