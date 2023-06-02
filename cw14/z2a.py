# Pod adresem httpbin.org na porcie TCP o numerze443działa serwer obsługujący protokół HTTPSw wersji1.1. Pod odnośnikiem/htmludostępnia prostą stronę HTML. Napisz program klienta, którypołączy się z serwerem, a następnie pobierze treść strony i zapisze ją na dysku jako plik z rozszerzeniem*.html. Spreparuj żądanie HTTP tak, aby serwer myślał, że żądanie przyszło od przeglądarki Safari7.0.3.
#

import socket
import ssl


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("httpbin.org", 443), )
    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23,
                        cert_reqs=ssl.CERT_NONE)

    s.sendall(
        b"GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Safari/7.0.3\r\n\r\n")

    data = s.recv(1024)

    length = data.decode("utf-8").split("Content-Length: ")[1].split("\r\n")[0]

    print(data.decode("utf-8"))

    with open("httpbin2.html", "w") as f:
        while length > 0:
            data = s.recv(1024)
            f.write(data.decode("utf-8"))
            length -= len(data)


if __name__ == "__main__":
    main()
