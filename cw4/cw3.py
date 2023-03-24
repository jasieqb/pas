#  Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie UDP,
# dla podłą-czającego się klienta, będzie odsyłał mu przesłaną wiadomość (tzw. serwer echa).
# Prawidłowa komunikacjapowinna odbywać się w nastepujacy sposób
# •Serwer odbiera dane od klienta
# •Serwer odsyła klientowi odebrane od niego dane

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))

while True:
    try:
        data, addr = s.recvfrom(1024)
        print('Connection from', addr)
        s.sendto(data, addr)
    except KeyboardInterrupt:
        s.close()

s.close()
