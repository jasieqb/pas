# Poniżej znajduje się pełny zapis datagramu UDP w postaci szesnastkowej.
# ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61
# 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f
# 6e 20 69 73 20 66 75 6e

# Wiedząc, że w zapisie szesnastkowym jedna cyfra reprezentuje 4 bity, oraz znając strukturę datagramu UDP:

# Napisz program, który z powyższego datagramu UDP wydobędzie:
# •numer źródłowego portu
# •numer docelowego portu
# •dane (ile bajtów w tym pakiecie zajmują dane?)A następnie uzyskany wynik w postaci:

# zad14odp;src;X;dst;Y;data;Z
# gdzie
# •X to wydobyty z pakietu numer portu źródłowego
# •Y to wydobyty z pakietu numer portu docelowego
# •Z to wydobyte z pakietu dane

# przykład:
# zad14odp;src;1234;dst;5678;data;programming in python is fun

# Wskazówka: w Pythonie możesz użyć funkcji int() do konwersji zapisu szesnastkowego na dziesiętny.

# Wskazówka: w Pythonie możesz użyć funkcji hex() do konwersji zapisu dziesiętnego na szesnastkowy.

# Wskazówka: w Pythonie możesz użyć funkcji bin() do konwersji zapisu dziesiętnego na binarny.

def parse_udp_packet(packet):
    src_port = int(packet[0:4], 16)
    dst_port = int(packet[4:8], 16)
    length = int(packet[8:12], 16)
    checksum = int(packet[12:16], 16)

    data = packet[16:]

    print(f'src_port: {src_port}')
    print(f'dst_port: {dst_port}')
    print(f'length: {length}')
    print(f'checksum: {checksum}')
    print(f'data: {data}')
    return f'zad14odp;src;{src_port};dst;{dst_port};data;{"".join([chr(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)])}'


def send_to_server(packet: str):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('localhost', 2910))
    sock.send(packet.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.close()


# def get_from_server():
#     import socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.connect(('212.182.25.252', 2910))
#     data = sock.recv(1024)
#     sock.close()
#     return data.decode('utf-8')


if __name__ == '__main__':
    udp_packet = 'ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e'
    print(parse_udp_packet(udp_packet))
    send_to_server(parse_udp_packet(udp_packet))
    # print("Received from server: ")
    # print(get_from_server())
