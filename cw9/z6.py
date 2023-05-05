# Zmodyfikuj program numer 3 z laboratorium numer 9 w taki sposób, aby program pobierał z serweraobrazek tylko wtedy, gdy nie zmienił się on od ostatniego pobrania. Jakich nagłówków HTTP należyużyć?

import socket


def get_image_if_change(host, port, path):
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
        # get actual image size from disk
        try:
            with open("cw9/image.png", "rb") as f:
                old_image = f.read()
                old_size = len(old_image)
        except FileNotFoundError:
            old_size = 0

        if old_size == size:
            print("Image not changed")
            s.close()
            return

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
    get_image_if_change("localhost", 80, "/image/png")
    # to nie jest idealne rozwiązanie bo nie sprawdzamy czy obrazek jest ten sam tylko czy ma taki sam rozmiar
    # można by to rozwiązać np. wykorzuystując pole nagłówka If-Modified-Since
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/
    # ale wygląda na to ze serwer nie obsługuje tego nagłówka
