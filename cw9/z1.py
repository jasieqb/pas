# Pod adresem httpbin.orgna porcie TCP o numerze80działa serwer obsługujący protokół HTTP w wersji1.1. Pod odnośnikiem/htmludostępnia prostą stronę HTML. Napisz program klienta, który połączy sięz serwerem, a następnie pobierze treść strony i zapisze ją na dysku jako plik z rozszerzeniem*.html.Spreparuj żądanie HTTP tak, aby serwer myślał, że żądanie przyszło od przeglądarkiSafari 7.0.3.Jakich nagłówków HTTP należy użyć?

import socket


def get_html(host, port, path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: Safari 7.0.3\r\n\r\n"
        s.send(request.encode())
        response = s.recv(4096)
        print(response.decode())
        # drop headers
        response = response.split(b"\r\n\r\n")[1]
        with open("cw9/index.html", "w+") as f:
            f.write(response.decode())


if __name__ == "__main__":
    get_html("httpbin.org", 80, "/html")
