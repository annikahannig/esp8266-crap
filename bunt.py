
"""
UDP server
"""

import time
import socket
import argparse

import config



def _open_socket(port):
    """
    Open UDP socket and bind to port.

    :param port: Bind the socket to this port
    :type port: int

    :returns: A bound socket
    :rtype: socket.socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", port))

    return s

