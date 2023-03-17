#  Poniżej znajduje się pełny zapis pakietu IP w postaci szesnastkowej (bez pola opcji IP, jeśli protokół toTCP, pole opcji TCP ma 12 bajtów).

# 45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b
# c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1
# 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01
# 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67
# 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e
# Wiedząc, że w zapisie szesnastkowym jedna cyfra reprezentuje 4 bity, oraz znając strukturę pakietu IP


# Napisz program, który z powyższego pakietu IP wydobędzie:
# •wersję protokołu•źródłowy adres IP
# •docelowy adres IP
# •typ protokołu warstwy wyższej:Numer protokołu TCP w polu
#   Protocolnagłówka IPv4 to 6 (0x06)
#   Numer protokołu UDP w polu Protocol nagłówka IPv4 to 17 (0x11)

# Oraz, po określeniu typu protokołu(TCP/UDP) dodatkowo wydobędzie z pakietu:
# •numer źródłowego portu
# •numer docelowego portu•dane(ile bajtów w tym pakiecie zajmują dane?)

# W przypadku pakietu TCP, dane to wszystkie bajty od 64. pozycji do końca pakietu.
# Klient wysyła do serwera wiadomość w postaci:
# zad15odpA;ver;X;srcip;Y;dstip;Z;type;W

# gdzie:
# •X to wydobyty z pakietu numer wersji protokołu•Y to wydobyty z pakietu źródłowy adres IP
# •Z to wydobyty z pakietu docelowy adres IP
# •W to wydobyty z pakietu typ protokołu warstwy wyższej(numer)

# b)  Klient odbiera od serwera wiadomość, która mówi o tym, czy odpowiedź jest prawidłowa, czy nie(c)
# Jeśli klient otrzyma od serwera odpowiedź TAK, może wysłać kolejną wiadomość do sprawdzenia wpostaci:

# zad15odpB;srcport;X;dstport;Y;data;Z
# b)  Klient odbiera od serwera wiadomość, która mówi o tym, czy odpowiedź jest prawidłowa, czy nie
# (c)  Jeśli klient otrzyma od serwera odpowiedź TAK, może wysłać kolejną wiadomość do sprawdzenia wpostaci:

# zad15odpB;srcport;X;dstport;Y;data;Z

# gdzie:
# •X to wydobyty z pakietu numer portu źródłowego
# •Y to wydobyty z pakietu numer portu docelowego
# •Z to wydobyte z pakietu dane
import socket


def parse_ip_packet(packet: str):
    version = int(packet[0:1], 16)
    print(version)

    src_addr_1 = int(packet[24:26], 16)
    src_addr_2 = int(packet[26:28], 16)
    src_addr_3 = int(packet[28:30], 16)
    src_addr_4 = int(packet[30:32], 16)

    src_addr = f'{src_addr_1}.{src_addr_2}.{src_addr_3}.{src_addr_4}'

    dst_addr_1 = int(packet[32:34], 16)
    dst_addr_2 = int(packet[34:36], 16)
    dst_addr_3 = int(packet[36:38], 16)
    dst_addr_4 = int(packet[38:40], 16)

    dst_addr = f'{dst_addr_1}.{dst_addr_2}.{dst_addr_3}.{dst_addr_4}'

    protocol = int(packet[18:20], 16)

    return version, protocol, src_addr, dst_addr


if __name__ == '__main__':
    # 45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b
    # c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1
    # 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01
    # 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67
    # 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e
    packet = '4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e'

    version, protocol, src_ip_addr, dst_ip_addr = parse_ip_packet(packet)
    odpA = f'zad15odpA;ver;{version};srcip;{src_ip_addr};dstip;{dst_ip_addr};type;{protocol}'
    print(odpA)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('212.182.25.252', 2911))
    sock.send(odpA.encode('utf-8'))
    data = sock.recv(1024)
    data = data.decode('utf-8')
    print(data)

    if data == "TAK":
        src_port = int(packet[40:44], 16)
        dst_port = int(packet[44:48], 16)
        data = packet[104:]
        data = bytes.fromhex(data).decode('utf-8')

        odpB = f'zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}'
        print(odpB)
        sock.send(odpB.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))

    sock.close()
