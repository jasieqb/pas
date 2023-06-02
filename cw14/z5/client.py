import ssl
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 12345))

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    # ctx.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # ctx.load_verify_locations("cert.pem")
    s = ctx.wrap_socket(s, server_hostname="localhost")

    cert = s.getpeercert()

    print(cert)

    s.sendall(b"Hello world")
    data = s.recv(1024)

    print(data.decode("utf-8"))

    s.close()


if __name__ == "__main__":
    main()
