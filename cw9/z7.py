# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP, będzieserwerem HTTP. Obsłuż wybrane nagłówki i co najmniej jeden kod błędu (np.404). Jako przykładowepliki serwera (stronę główną i stronę błędu) możesz wykorzystać pliki dostępne na stronie przedmiotu

import socket


def run_simple_http(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print("Server started")
            print(f"Listening on {host}:{port}")
            while True:
                conn, addr = s.accept()
                print("=====================================")
                with conn:
                    print('Connected by', addr)
                    data = b""
                    while b"\r\n\r\n" not in data:
                        data += conn.recv(2048)
                    headers = data.split(b"\r\n\r\n")[0]
                    print("Incoming headers:")
                    print(headers.decode())
                    path = headers.split(b" ")[1]
                    print(f"Requested path: {path.decode()}")
                    if path == b"/":
                        path = b"/index.html"

                    try:
                        with open("cw9/assets" + path.decode(), "rb") as f:
                            content = f.read()
                            conn.send(b"HTTP/1.1 200 OK\r\n")
                            conn.send(b"Content-Type: text/html\r\n")
                            conn.send(b"Content-Length: " +
                                      str(len(content)).encode() + b"\r\n")
                            conn.send(b"\r\n")
                            conn.send(content)

                    except FileNotFoundError:
                        conn.send(b"HTTP/1.1 404 Not Found\r\n")
                        conn.send(b"Content-Type: text/html\r\n")
                        conn.send(b"\r\n")
                        conn.send(b"<h1>404 Not Found</h1>")
    except KeyboardInterrupt:
        print("Interrupted")


if __name__ == "__main__":
    run_simple_http("localhost", 8083)
