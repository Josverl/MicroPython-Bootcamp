import network
import socket

import machine
import time

#wlan = network.WLAN()
#wlan.active(True)
#wlan.connect('my_ap','my_password')

sock_listen = socket.socket()
sock_listen.bind(('0.0.0.0', 9999))
sock_listen.listen(1)

touch0 = machine.TouchPad(machine.Pin(4))
touch2 = machine.TouchPad(machine.Pin(2))
touch4 = machine.TouchPad(machine.Pin(13))
touch5 = machine.TouchPad(machine.Pin(12))
touch6 = machine.TouchPad(machine.Pin(14))

help(machine)
help(machine.TouchPad)

touch2
touch2.read()

touch0
touch0.read()


touch2  
.config(600)
touch0.read()

import time,machine
touch2 = machine.TouchPad(machine.Pin(2))
for n in range(10):
    touch2.read()
    time.sleep(0.2)






print('done')



while True:
    try:
        sock, _  = sock_listen.accept()
        start_ticks = time.ticks_ms()
        while True:
            sock.write("%d %d %d %d %d %d\n" % (
                time.ticks_diff(time.ticks_ms(), start_ticks),
                touch0.read(),
                touch2.read(),
                touch4.read(),
                touch5.read(),
                touch6.read()
            ))
            time.sleep(0.01)
    except OSError:
        pass
