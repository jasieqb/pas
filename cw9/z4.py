# Pod adresemhttpbin.orgna porcie TCP o numerze 80 działa serwer obsługujący protokół HTTP wwersji 1.1. Pod odnośnikiem/postudostępnia formularz z polami do wypełnienia.Napisz program klienta, który połączy się z serwerem, a następnie uzupełni formularz danymi pobranymiod użytkownika, a następnie prześle go do serwera i odbierze odpowiedź.Aby sprawdzić, jak wygląda żądanie HTTP potrzebne do wypełnienia i wysłania formularza:
# •jakienagłówki HTTPsą wykorzystywane,
# •jak wygląda ciało zapytania,
# podsłuchaj komunikację z serwerem za pomocą Wiresharka, tj. uruchom przeglądarkę oraz Wiresharka;uzupełnij i zatwierdź formularz ręcznie za pomocą przeglądarki, a następnie sprawdź pakiety podsłucha-ne podczas komunikacji z serweremhttpbin.org. Możesz użyć filtrów Wiresharka:http.requestorazhttp.response(http.request||http.response).

# formularz nie istnieje :/

import socket
import time


def post_to_serve(host, port, path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        to_send = input("Enter data to send (value1): ")
        to_send = 'x=' + to_send + '&y=' + \
            input("Enter data to send (value2): ")
        size_to_send = len(to_send)

        request = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nAccept: */*\r\nConnection: keep-alive\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {size_to_send}\r\n\r\n{to_send}"
        s.send(request.encode())

        print("Sending...")
        print(request)

        print("Receiving...")
        time.sleep(5)
        data = b""
        data = s.recv(4096)

        print(len(data))
        print(data.decode())


if __name__ == "__main__":
    post_to_serve("localhost", 80, "/post")
