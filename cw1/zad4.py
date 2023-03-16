import socket


def get_name_for_ip_adress(ip_address: str):
    return socket.gethostbyaddr(ip_address)


def main():
    ip_address = input("Podaj adres ip: ")
    print(get_name_for_ip_adress(ip_address))


if __name__ == "__main__":
    main()
