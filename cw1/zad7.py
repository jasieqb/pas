import socket


def check_all_ports(ip):
    for port in range(1, 65535):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((ip, port))
            print("Port {} otwarty".format(port))
            s.close()
        except KeyboardInterrupt:
            exit()
        except:
            pass


if __name__ == "__main__":
    check_all_ports("212.182.25.252")
