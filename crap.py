
"""
UDP server
"""

import time
import socket

import config



def open_socket(port):
    """Open UDP socket and bind to port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", port))

    return s


def recv_frame(s):
    """Receive a single frame of CRAP rgb data"""
    frame_size = config.MAX_LEDS * 3
    data, _ = s.recvfrom(frame_size)

    return data


