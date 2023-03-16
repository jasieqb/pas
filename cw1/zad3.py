from ipaddress import ip_address


def check_ip(ip: str) -> bool:
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False


def main():
    ip = input("Podaj adres IP: ")
    if check_ip(ip):
        print("Adres IP jest poprawny")
    else:
        print("Adres IP jest niepoprawny")


if __name__ == "__main__":
    main()
