import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1234))
        while True:
            data = input('Enter a number: ')
            s.sendall(data.encode())
            data = s.recv(1024)
            print(data.decode())
            if data == b'CORRECT!':
                break

        print('Connection closed')

if __name__ == '__main__':
    main()
