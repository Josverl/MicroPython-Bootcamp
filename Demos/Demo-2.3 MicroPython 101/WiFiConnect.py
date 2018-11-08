# network module
#This module provides access to various network related functions and classes.

import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)                   # activate the interface
wlan.scan()                         # scan for access points

if not wlan.isconnected():                  # check if the station is connected to an AP
    wlan.connect('IOTBOOTCAMP', 'MicroPython')   # connect to an AP

if wlan.isconnected():                  # check if the station is connected to an AP
    wlan.ifconfig()                     # get the interface's IP/netmask/gw/DNS addresses
