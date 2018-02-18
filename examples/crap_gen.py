
import socket

MAX_LEDS = 70

BUF_SIZE = MAX_LEDS * 3

def connect(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        host, port = addr.split(":")
    except:
        raise ValueError("Address needs to be in format host:port")

    return (sock, (host, int(port)))


def send(conn, data):
    sock = conn[0]
    addr = conn[1]

    sock.sendto(data, addr)





