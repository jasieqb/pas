# Napisz program, który z serwera ntp.task.gda.pl pobierze aktualną datę i czas, a następnie wyświetli jena konsoli. Serwer działa na porcie 13.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("ntp.task.gda.pl", 13))
data = s.recv(1024)
s.close()
print(data)
