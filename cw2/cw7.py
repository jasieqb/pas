import socket
import argparse

argparser = argparse.ArgumentParser()
# argparser.add_argument("-n", "--name", help="Podaj adres name")
argparser.add_argument("-i", "--ip", help="Podaj adres ip")
argparser.add_argument("-p", "--port", help="Podaj port")
args = argparser.parse_args()


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((args.ip, int(args.port)))
if soc:
    print(f"Połączono, usługa to: {socket.getservbyport(int(args.port))}")
else:
    print("Nie połączono")
    exit()
print(soc.recv(1024))
