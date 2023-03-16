import socket


def get_ip(name: str):
    return socket.gethostbyname(name)


def main():
    name = input("Podaj adres name: ")
    print(get_ip(name))


if __name__ == "__main__":
    main()
