
"""
UDP server
"""

import time
import socket

import machine
import neopixel

import config


LEDS_PIN = machine.Pin(0, machine.Pin.OUT)
LEDS = neopixel.NeoPixel(LEDS_PIN, config.MAX_LEDS)


def _open_socket(port):
    """Open UDP socket and bind to port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))

    return s


def _recv_frame(s):
    """Receive a single frame of CRAP rgb data"""
    frame_size = config.MAX_LEDS * 3
    data, _ = s.recvfrom(frame_size)

    return data


def receive(port):
    sock = _open_socket(port)

    while True:
        frame = _recv_frame(sock)
        if len(frame) < config.MAX_LEDS*3:
            print("received framelength {}".format(len(frame)))
            continue

        # Update ws2812
        for i in range(0, config.MAX_LEDS):
            r = frame[i*3]
            g = frame[i*3+1]
            b = frame[i*3+2]

            LEDS[i] = (r,g,b)

        LEDS.write()
