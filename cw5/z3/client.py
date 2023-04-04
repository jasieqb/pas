# Port-knocking jest metodą pozwalającą na nawiązanie zdalnego połączenia z usługami działającymi
# na komputerze, do którego dostęp został ograniczony np. za pomocą zapory sieciowej, umożliwiającą
# odróżniania prób połączeń, które powinny i nie powinny być zrealizowane. Inaczej mówiąc, to metoda
# ustanawiania połączenia z hostem o zamkniętych portach.
# Pod adresem 212.182.24.27 na porcie TCP o numerze 2913 działa ukryta usługa. Usługa jest zabezpieczona
# metodą port knocking - po otrzymaniu od klienta odpowiedniej sekwencji pakietów UDP na odpowiednie
# porty, otwiera wspomniany wyżej port TCP. Napisz program klienta, który odgadnie sekwencję portów
# UDP, a następnie odbierze od serwera wiadomość na porcie TCP.
# Uwaga: Aby znaleźć porty UDP, składające się na sekwencję otwarcia docelowego portu TCP, wysyłaj
# do serwera wiadomość o treści PING. W przypadku, gdy uda się znaleźć port UDP, należący do sekwencji
# otwierającej port TCP, serwer odeśle wiadomość PONG. Porty UDP, które wchodzą w skład sekwencji
# kończą się na 666. Usługa działająca na ukrytym porcie, jeśli uda się ją znaleźć, zwraca w odpowiedzi
# tekst: Congratulations! You found the hidden.

import socket
from time import sleep

from itertools import permutations


def knock():
    # ports ending with 666
    ports_list = []
    for i in range(0, 65):
        ports_list.append(i * 1000 + 666)

    print(ports_list)

    good_ports = []

    for port in ports_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(5)
        try:
            s.connect(('localhost', port))
            s.send('PING'.encode('utf-8'))
            data = s.recv(1024)
            if data == b'PONG':
                print(f'Found port: {port}')
                good_ports.append(port)
            else:
                print(f'received {data} from')
        except Exception as e:
            print(f'Port {port} not found with error: {str(e)}')
            continue

        s.close()

    print(f'Good ports: {good_ports}')

    perms = permutations(good_ports, 3)
    sleep(2)
    for perm in perms:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(3)
        try:
            s.connect(('127.0.0.1', perm[0]))
            s.send('PING'.encode('utf-8'))
            sleep(1)
            data = s.recv(1024)
            if data == b'PONG':
                print(f'Found port: {perm[0]}')
                s.connect(('127.0.0.1', perm[1]))
                s.send('PING'.encode('utf-8'))
                sleep(1)
                data = s.recv(1024)
                if data == b'PONG':
                    print(f'Found port: {perm[1]}')
                    s.connect(('127.0.0.1', perm[2]))
                    s.send('PING'.encode('utf-8'))
                    sleep(1)
                    data = s.recv(1024)
                    if data == b'PONG':
                        print(f'Found port: {perm[2]}')
                        try:
                            soclast = socket.socket(
                                socket.AF_INET, socket.SOCK_STREAM)
                            soclast.connect(('127.0.0.1', 2913))
                            soclast.send('PING'.encode('utf-8'))
                            data = soclast.recv(1024)
                            print(data.decode())

                        except Exception as e:
                            print(
                                f'LAST {perm} not found with error: {str(e)}')
                            continue

                        # break
        except Exception as e:
            print(f'Port {perm} not found with error: {str(e)}')
            continue
        s.close()
    print(f'Ended with {perm}')


def main():
    # knock()
    print('Knocking finished')

    soc1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc1.settimeout(3)
    soc1.connect(('127.0.0.1', 34666))
    soc1.send('PING'.encode('utf-8'))
    sleep(1)
    print(soc1.recv(1024).decode())
    # soc1.close()

    # soc2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # soc2.settimeout(1)
    soc1.connect(('127.0.0.1', 17666))
    soc1.send('PING'.encode('utf-8'))
    print(soc1.recv(1024).decode())
    # soc1.close()

    # soc3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # soc3.settimeout(1)
    soc1.connect(('127.0.0.1', 53666))
    soc1.send('PING'.encode('utf-8'))
    print(soc1.recv(1024).decode())
    soc1.close()

    sleep(1)

    last_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    last_soc.settimeout(2)
    last_soc.connect(('127.0.0.1', 2913))
    last_soc.send('PING'.encode('utf-8'))
    print(last_soc.recv(1024).decode())
    last_soc.close()


if __name__ == '__main__':
    main()
