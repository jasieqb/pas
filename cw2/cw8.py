# Zmodyfikuj program numer 7 z laboratorium nr 1 w ten sposób, aby oprócz wyświetlania informacji otym, czy porty są jest zamknięte, czy otwarte, klient wyświetlał również informację o tym, jaka usługajest uruchomiona na danym porcie.

import socket


def check_all_ports(ip):
    for port in range(1, 65535):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((ip, port))
            print(f"Port {port} otwarty, Usługa: {socket.getservbyport(port)}")

            s.close()
        except KeyboardInterrupt:
            exit()
        except:
            pass

        if port % 100 == 0:
            print("Sprawdzono porty: {}".format(port))


if __name__ == "__main__":
    check_all_ports("212.182.25.252")
