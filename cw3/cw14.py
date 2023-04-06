# Poniżej znajduje się pełny zapis segmentu TCP w postaci szesnastkowej (pole opcji ma 12 bajtów).
# 0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18
# 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee
# 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29
# Wiedząc, że w zapisie szesnastkowym jedna cyfra reprezentuje 4 bity, oraz znając strukturę segmentu TCP:
# Napisz program, który z powyższego segmentu TCP wydobędzie:
# •numer źródłowego portu
# •numer docelowego portu
# •dane (ile bajtów w tym pakiecie zajmują dane?)
# A następnie uzyskany wynik w postaci:
#
# zad13odp;src;X;dst;Y;data;Z
# gdzie:
# •X to wydobyty z pakietu numer portu źródłowego
# •Y to wydobyty z pakietu numer portu docelowego
# •Z to wydobyte z pakietu dane

def parse_tcp_packate(packet: str):
    src_port = int(packet[0:4], 16)
    dst_port = int(packet[4:8], 16)
    data = packet[64:]
    data = "".join([chr(int(data[i:i + 2], 16))
                   for i in range(0, len(data), 2)])

    print(f'src_port: {src_port}')
    print(f'dst_port: {dst_port}')
    print(f'data: {data}')
    return f'zad13odp;src;{src_port};dst;{dst_port};data;{data}'


def send_to_server(packet: str):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('localhost', 2909))
    sock.send(packet.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.close()


# def get_from_server():
#     import socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('212.182.25.252', 2910))
#     data = sock.recv(1024)
#     sock.close()
#     return data.decode('utf-8')


if __name__ == '__main__':
    packet = '0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4ce668656c6c6f203a29'
    print(parse_tcp_packate(packet))
    send_to_server(parse_tcp_packate(packet))
