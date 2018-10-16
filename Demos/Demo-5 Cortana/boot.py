# This file is executed on every boot (including wake-boot from deepsleep)
#-----------------------------------------------------
# .) Init Display
# 1) connect to the network details stored in myconfig 
#    beep if no network connection
# 2) if connect , get the network time
# 3) load utility functions from upysh 
#
# x) start ftp server 
#-----------------------------------------------------
# add path to library folder in flash
try:
    import sys
    sys.path[1] = '/flash/lib'
    mkdir('/flash/lib')
except:
    pass 
#helper functions    
def log(message):
    print(message)
    
# Connect to WiFi 
def connect_wifi():
    "Connect to WiFi"
    import network, time
    #read network info from : myconfig.py
    try:
        from myconfig import wifi_ssid , wifi_psk
    except:
        print('No Network configuration file found')
        #todo: show help how to create one 
        return False
    wlan = network.WLAN(network.STA_IF)
    tmo = 80
    if not wlan.isconnected():
        print('connecting to network : {}'.format(wifi_ssid))
        wlan.active(True)
        wlan.connect(wifi_ssid, wifi_psk)
        #Wait for WiFi connection 
        while not wlan.isconnected():
            if tmo == 0:
                break
            print(".", end="")
            tmo -= 1
            time.sleep_ms(200)
        print()
    try: 
        log( 'IP: {}'.format( wlan.ifconfig()[0]  ))
        return True
    except:
        pass
    if not wlan.isconnected():
        beepSad()
        return False

def get_network_time(timezone = "CET-1CEST"):
    "get time via NTP for Central Europe"
    # Lobo Specific 
    import machine
    rtc = machine.RTC()
    rtc.init((2018, 01, 01, 12, 12, 12))
    rtc.ntp_sync(server= "", tz=timezone, update_period=3600)
    #need to wait a bit 
    tmo = 100
    while not rtc.synced():
        tmo=tmo-1
        if tmo==0:
            break
        time.sleep_ms(10)

#simplify filesystem access from the prompt
from upysh import *

# Connect to WiFi 
log('Connect to WiFi...')
connected = connect_wifi()
if connected:
    #log('Get network Time...')
    get_network_time()
    fmt="%d-%m-%Y, %T %Z" #Europe
    #fmt="%b %d %Y, %r %Z" #US
    log(time.strftime(fmt,time.localtime()))

    #allow the board to be reached via telnet
    try:
        import network
        network.telnet.start(user="micro", password="python", timeout=300)
    except:
        pass

import gc
gc.collect()
