# Funkcje recv i send nie gwarantują wysłania / odbioru wszystkich danych. Rozważmy funkcję recv.
# Przykładowo, 100 bajtów może zostać wysłane jako grupa po 10 bajtów, albo od razu w całości. Oznacza
# to, iż jeśli używamy gniazd TCP, musimy odbierać dane, dopóki nie mamy pewności, że odebraliśmy
# odpowiednią ich ilość. Zmodyfikuj program nr 11 z laboratorium nr 2 w ten sposób, aby mieć pewność,
# że klient w rzeczywistości odebrał / wysłał wiadomość o wymaganej długości.

# zadanie 11
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("212.182.25.252", 2908))
# message = "Hello, server!"

# if len(message) < 20:
#     message = message.ljust(20)
# elif len(message) > 20:
#     message = message[:20]

# s.send(message.encode())
# data = s.recv(1024)
# s.close()
# print(data)


# rozwiązanie

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.25.252", 2908))
message = "Hello, server!"

if len(message) < 20:
    message = message.ljust(20)

elif len(message) > 20:
    message = message[:20]
data = b""
for i in range(20):
    s.send(message[i].encode('utf-8'))
    data += s.recv(20).decode('utf-8')

s.close()
print(data)
