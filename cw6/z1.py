# Wykorzystując protokół telnet, oraz serwer ESMTP działający pod adreseminteria.plna porcie587wyślij wiadomość e-mail używając komend protokołu ESMTP.

import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("interia.pl", 587))
    print(s.recv(1024).decode("utf-8"))
    s.send("HELO interia.pl\r
