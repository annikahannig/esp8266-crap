
import time

import network
import machine

import config

STATUS_LED = machine.Pin(16, machine.Pin.OUT)
WIFI_LED = machine.Pin(2, machine.Pin.OUT)

# Initial state
STATUS_LED.value(1)
WIFI_LED.value(1)


def connect(max_retries=10):
    retries = 0

    # We are not connected, blue led off
    WIFI_LED.value(1)
    STATUS_LED.value(0)

    # Connect wifi
    nic = network.WLAN(network.STA_IF)
    nic.active(True)

    if config.WIFI_IFCONFIG:
        nic.ifconfig(config.WIFI_IFCONFIG)

    while not nic.isconnected():
        # Blink led
        STATUS_LED.value(not STATUS_LED.value())
        time.sleep(0.5)

        nic.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

        retries += 1
        if retries > max_retries:
            return False

    # We are connected
    WIFI_LED.value(0)

    return nic.ifconfig()
