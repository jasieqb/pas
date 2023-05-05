# Pod adresem212.182.24.27na porcie TCP o numerze8080działa serwer obsługujący protokół HTTP wwersji 1.1. Pod odnośnikiem/image.jpgudostępnia obrazek. Napisz program klienta, który połączy sięz serwerem, a następnie pobierze z serwera obrazek w3częściach i po odebraniu wszystkich części złożygo w całość. Jakich nagłówków HTTP należy użyć?


# serwer nie dział :/
# użycie localhost zamiast zdalnego ip
import socket


def get_png_3_parts(host, port, path):
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
        parts_size = size // 3

        for i in range(3):
            while len(response) < parts_size * (i + 1):
                response += s.recv(1024)
                print("recv: ", len(response))
        # save image
        print("Saving...")
        print(response)
        with open("cw9/image2.png", "wb+") as f:
            f.write(response)
        print("Done")


if __name__ == "__main__":
    get_png_3_parts("localhost", 80, "/image/png")
