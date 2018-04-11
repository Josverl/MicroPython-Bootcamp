# network module
#This module provides access to various network related functions and classes.

import network

wlan = network.WLAN(network.STA_IF) # create station interface

wlan.active(True)                   # activate the interface
wlan.scan()                         # scan for access points
wlan.isconnected()                  # check if the station is connected to an AP
wlan.connect('Atticware', '!!DAF66!!')   # connect to an AP

wlan.ifconfig()                     # get the interface's IP/netmask/gw/DNS addresses
