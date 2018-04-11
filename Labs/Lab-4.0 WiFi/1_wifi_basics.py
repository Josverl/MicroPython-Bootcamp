# network module
#This module provides access to various network related functions and classes.

import network

help(network)

# create station interface - Standard WiFi client 
wifi = network.WLAN(network.STA_IF) 
# activate the interface
wifi.active(True)
# scan for access points                   
wifi.scan()             

# connect to an AP
wifi.connect('IOTBOOTCAMP', 'MicroPython')   

# check if the station is connected to an AP            
wifi.isconnected()


# get the interface's IP/netmask/gw/DNS addresses
wifi.ifconfig()                     
