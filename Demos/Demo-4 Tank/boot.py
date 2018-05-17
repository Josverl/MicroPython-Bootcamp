"""
IoT Bootcamp - dfplayer.py 
Marcus Tarquinio, Jos Verlinde
28th Abril 2018

Modified from original Botdemy code
http://www.instructables.com/id/MicroPython-IoT-Rover-Based-on-WeMos-D1-ESP-8266EX/
"""
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl

def do_connect():
  import network
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.ifconfig(('192.168.8.200','255.255.255.0','192.168.8.1','192.168.8.1'))
    sta_if.connect('IOTBOOTCAMP','MicroPython')
    while not sta_if.isconnected():
      pass
  print('network config:', sta_if.ifconfig())

do_connect()
webrepl.start()
gc.collect()
