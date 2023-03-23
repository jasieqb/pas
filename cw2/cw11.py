# Zmodyfikuj program nr 2 z laboratorium nr 2 w ten sposób, aby klient wysłał i odebrał od serwera wia-
# domość o maksymalnej długości 20 znaków. Serwer TCP odbierający i wysyłający wiadomości o długości
# 20 działa pod adresem 212.182.24.27 na porcie 2908. Uwzględnij sytuacje, gdy:

# wiadomość do wysłania jest za krótka - ma być wówczas uzupełniania do 20 znaków znakami spacji
# wiadomość do wysłania jest za długa - ma być przycięta do 20 znaków(lub wysłana w całości -
#   sprawdź, co się wówczas stanie)

# program z zadania 2
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("212.182.25.252", 2900))
# s.send(b"Hello, server!")
# data = s.recv(1024)
# s.close()
# print(data)

# rozwiązanie

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.25.252", 2908))
message = "HELLO SERVER: LONG MESSAGE ......."

if len(message) < 20:
    message = message.ljust(20)
elif len(message) > 20:
    message = message[:20]

print(f'To sent: {message}')

s.send(message.encode())
data = s.recv(20)
s.close()
print(data)
