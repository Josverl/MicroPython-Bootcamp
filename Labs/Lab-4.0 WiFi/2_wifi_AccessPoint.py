# import the network module
# This module provides access to various network related functions and classes.
# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/network 

import network,time #pylint: disable=import-error

# create Access Point interface 
ap = network.WLAN(network.AP_IF) 
# activate the interface
ap.active(True)

# Wait until started and show IF config
# We don't need to check for connected clients
# so we give the False argument
tmo = 50
while not ap.isconnected(False):
    utime.sleep_ms(100)
    tmo -= 1
    if tmo == 0:
        break
print("\n=== AP started =====================\n")

print("This ESP32 Access point is")
print("Network {}, Channel {}, security: {}, mode:{}".format( 
    ap.config('essid'),
    ap.config('channel'),
    ap.config('authmode'),
    ap.config('wifimode'),
))
print("IP:{0}, Network mask:{1}, Router:{2}, DNS: {3}".format( *ap.ifconfig() ) )

#Note: it is not possible the retrieve the password from the AccessPoint 


bonus = False
if bonus:
    #==================================================================================
    # Change some Acess Point parameters
    # AP will stop than started with new parameters
    print("\n=== Change AP parameters ===========\n")
    ap.config(essid='<MYNAME>', authmode=network.AUTH_WPA_WPA2_PSK, password='12345678')

    time.sleep_ms(200)
    # Wait until started and show IF config
    # We don't need to check for connected clients
    # so we give the False argument
    tmo = 50
    while not ap.isconnected(False):
        time.sleep_ms(100)
        tmo -= 1
        if tmo == 0:
            break
    print("\n=== AP ReStarted ===================\n")

    print("This ESP32 Access point is")
    print("Network {}, Channel {}, security: {}, mode:{}".format( 
        ap.config('essid'),
        ap.config('channel'),
        ap.config('authmode'),
        ap.config('wifimode'),
    ))
    print("IP:{0}, Network mask:{1}, Router:{2}, DNS: {3}".format( *ap.ifconfig() ) )

    # ==================================================================================
    #todo: Change to a different Wifi Channel 
    # Refer to : https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/network 
    # > To set the parameter(s) use wlan.config(arg=value [,arg1=value1 [, .... ]]) format, multiple arguments can be entered.

     