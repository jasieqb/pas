# Napisz program serwera, który działajac pod adresem127.0.0.1oraz na określonym porcie TCP, dlapodłaczającego się klienta, będzie odsyłał mu przesłaną wiadomość(tzw. serwer echa). Serwer powinienwykorzystywać samodzielnie podpisany(self-signed) certyfikat, który możesz wygenerować za pomocąbibliotekiOpenSSL.

import socket
import ssl


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 12345))
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    s.listen(1)

    s = ctx.wrap_socket(s, server_side=True)
    while True:
        conn, addr = s.accept()

        print("Connected by", addr)
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
        conn.close()


if __name__ == "__main__":
    main()
