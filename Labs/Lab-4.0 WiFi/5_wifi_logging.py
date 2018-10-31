# import the network module
# This module provides access to various network related functions and classes.
# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/network 

import network,utime #pylint: disable=import-error

# ----------------------------------------------------------
# Define callback function used for monitoring wifi activity
# ----------------------------------------------------------


'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
'''


def wifi_cb(info):
    _red = "\033[31m"
    _cyan= "\033[36m"
    _norm = "\033[00m"
    if (info[2]):
        msg = ", info: {}".format(info[2])
    else:
        msg = ""
    print(_cyan+"I [WiFi] event: {} ({}){}".format( info[0], info[1], msg)+_norm)

# Enable callbacks
network.WLANcallback(wifi_cb)                    

# ----------------------------------------------------------
# create station interface - Standard WiFi client 
wlan = network.WLAN(network.STA_IF) 
wlan.active(False)

# activate the interface
wlan.active(True)

# connect to a known WiFi 
wlan.connect('IOTBOOTCAMP', 'MicroPython')   

# Note that this may take some time, so we need to wait 
# Wait 5 sec or until connected 
tmo = 50
while not wlan.isconnected():
    utime.sleep_ms(100)
    tmo -= 1
    if tmo == 0:
        break

# check if the station is connected to an AP            
if wlan.isconnected(): 
    print("=== Station Connected to WiFi \n")
else:
    print("!!! Not able to connect to WiFi")

# gets or sets the interface's IP/netmask/gw/DNS addresses
# 'Raw'
print( wlan.ifconfig() )

#pretty
c = wlan.ifconfig()
print("IP:{0}, Network mask:{1}, Router:{2}, DNS: {3}".format( *c ))


