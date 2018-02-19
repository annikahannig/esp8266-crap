
import machine

import wifi
import crap


res = wifi.connect()
if res == False:
    print("Could not connect to WIFI")
    machine.reset()

crap.receive(1338)

