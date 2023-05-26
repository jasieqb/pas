# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP będzieobsługiwał protokół WebSocket. Możesz ograniczyć się do wysyłania/odbierania danych w postaci teksto-wej.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1236))
s.listen(5)

while True:
    sock, addr = s.accept()
    print('Connected:', addr)
    # check if upgrade to websocket
    data = sock.recv(1024)
    if data:
        print(data)
        if b'Upgrade: websocket' in data:
            print('Websocket')
            # send response
            response = b'HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r\n\r\n'
            sock.send(response)
            # receive data
            data = sock.recv(1024)
            print(data)
            # send data
            sock.send(b'Hello from server')
            while True:
                data = sock.recv(1024)
                print(data)
                sock.send(data)
        else:
            print('Not websocket')
            sock.send(b'Not websocket')
            sock.close()

s.close()
