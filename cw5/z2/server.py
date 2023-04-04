# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP będzie
# losował liczbę i odbierał od klienta wiadomości. W przypadku, gdy w wiadomości klient przyśle do serwera
# coś innego, niż liczbę, serwer powinien poinformować klienta o błędzie. Po odebraniu liczby od klienta,
# serwer sprawdza, czy otrzymana liczba jest:
# • mniejsza od wylosowanej przez serwer
# • równa wylosowanej przez serwer
# • większa od wylosowanej przez serwer
# A następnie odsyła stosowną informację do klienta. W przypadku, gdy klient odgadnie liczbę, serwer
# powinien zakończyć działanie.

import socket
import random


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 1234))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            random_number = random.randint(0, 100)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    data = int(data)
                    if data == random_number:
                        conn.sendall(b'CORRECT!')
                        exit("Correct number!")

                    elif data > random_number:
                        conn.sendall(b'Your number is too big')
                    else:
                        conn.sendall(b'Your number is too small')
                except ValueError:
                    conn.sendall(b'You did not send a number')


if __name__ == '__main__':
    main()
