# Pod adresem httpbin.org na porcie TCP o numerze443działa serwer obsługujący protokół HTTPSw wersji1.1. Pod odnośnikiem/htmludostępnia prostą stronę HTML. Napisz program klienta, którypołączy się z serwerem, a następnie pobierze treść strony i zapisze ją na dysku jako plik z rozszerzeniem*.html. Spreparuj żądanie HTTP tak, aby serwer myślał, że żądanie przyszło od przeglądarki Safari7.0.3.
#
# Klient weryfikuje tożsamość serwera


import socket
import ssl


def main():

    with socket.create_connection(("httpbin.org", 443)) as sock:

        ctx = ssl.create_default_context()

        ctx.check_hostname = True
        ctx.verify_mode = ssl.CERT_REQUIRED
        ctx.load_default_certs()

        s = ctx.wrap_socket(sock, server_hostname="httpbin.org")

        cert = s.getpeercert()

        if not cert or ssl.match_hostname(cert, "httpbin.org"):
            print("ERROR: Invalid certificate")
            return

        s.sendall(
            b"GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Safari/7.0.3\r\n\r\n")
        data = s.recv(1024)
        print(data.decode("utf-8"))
        length = 0
        while True:
            data = s.recv(1024)
            if not data:
                break
            length += len(data)
            print(data.decode("utf-8"))

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("httpbin.org", 443), )
    # s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_2,
    #                     cert_reqs=ssl.CERT_REQUIRED)

    # cert = s.getpeercert()

    # if not cert or ssl.match_hostname(cert, "httpbin.org"):
    #     print("ERROR: Invalid certificate")
    #     s.close()

    # s.sendall(
    #     b"GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Safari/7.0.3\r\n\r\n")

    # data = s.recv(1024)

    # print(data.decode("utf-8"))

    # length = 0
    # while True:
    #     data = s.recv(1024)
    #     if not data:
    #         break
    #     length += len(data)
    #     print(data.decode("utf-8"))


if __name__ == "__main__":
    main()
