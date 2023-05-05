# Pod adresem httpbin.orgna porcie TCP o numerze80działa serwer obsługujący protokół HTTP wwersji1.1. Pod odnośnikiem/image/pngudostępnia obrazek. Napisz program klienta, który połączy się z serwerem, a następnie pobierze obrazek i zapisze go na dysku. Jakich nagłówków HTTP należy użyć?

import socket


def get_png(host, port, path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        s.send(request.encode())

        # get headers
        data = b""
        while b"\r\n\r\n" not in data:
            data += s.recv(2048)
        headers = data.split(b"\r\n\r\n")[0]
        size = int(headers.split(b"Content-Length: ")[1].split(b"\r\n")[0])
        print(headers.decode())
        print(size)
        # get image
        response = b''
        while len(response) < size:
            response += s.recv(1024)
            print("recv: ", len(response))

        # save image
        print("Saving...")
        print(response)
        with open("cw9/image.png", "wb+") as f:
            f.write(response)
        print("Done")


if __name__ == "__main__":
    get_png("localhost", 80, "/image/png")
