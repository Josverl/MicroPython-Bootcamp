# import the network module
# This module provides access to various network related functions and classes.
# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/network 

import network,utime #pylint: disable=import-error
dir(network)

# create station interface - Standard WiFi client 
wlan = network.WLAN(network.STA_IF) 

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
config = wlan.ifconfig()

# 'Raw'
print( config )

#pretty
c = wlan.ifconfig()
print("IP:{0}, Network mask:{1}, Router:{2}, DNS: {3}".format( *config ))


bonus = False
if bonus:
    #Change the network settings , 
    # ie change the IP address you have been assigned to a different
    # If the config argument is given (as tuple (ip_address, net_mask, gateway_ip, DNS_ip)), 
    # sets the static IP configuration.
    wlan.ifconfig( ('192.168.10.5', '255.255.255.0', '192.168.10.1', '192.168.10.1') )

    #get other configuration 
    wlan.config('all') 


    #Get curent time from the internet
    #Note : The Loboris firmware works different from standard Micropython 
    # reference : https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/rtc
    from machine import RTC
    # Timezone is found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
    timezone = 'CET-1CEST'
    rtc = RTC()
    #Set the system time and date, (in this case very roughly).
    rtc.init((2018, 01, 01, 12, 12, 12))
    #configure to sync the time every hour with a Network Time Protocol (NTP) server
    rtc.ntp_sync(server= "", tz=timezone, update_period=3600)
    #is the time synched ?
    rtc.synced()
    #get the current,synchonized, time 
    rtc.now()
