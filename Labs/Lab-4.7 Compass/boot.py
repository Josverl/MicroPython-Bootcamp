
# This file is executed on every boot (including wake-boot from deepsleep)

#-----------------------------------------------------
# connect to the network details stored in myconfig 
# if no connection is possible , then re-start as an 
# accesspoint using the same config 
#-----------------------------------------------------

def do_connect():
    import network, time
    #read network info from : myconfig.py
    wifi_AutoAP=True
    from myconfig import wifi_ssid , wifi_psk
    wlan = network.WLAN(network.STA_IF)
    tmo = 50
    if not wlan.isconnected():
        print('connecting to network : {}'.format(wifi_ssid))
        wlan.active(True)
        wlan.connect(wifi_ssid, wifi_psk)
        #Wait for WiFi connection 
        while not wlan.isconnected():
            if tmo == 0:
                break
            #BlinkLed(led)
            print(".", end="")
            tmo -= 1
            time.sleep_ms(200)
        print()
    if tmo!=0: 
        print('network config:', wlan.ifconfig())

def get_networktime():
    import machine
    my_timezone = "CET-1CEST" # found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
    rtc = machine.RTC()
    rtc.init((2018, 01, 01, 12, 12, 12))
    rtc.ntp_sync(server= "", tz=my_timezone, update_period=3600)
# Now do the actual work
import sys
sys.path[1] = '/flash/lib'
from upysh import * 


do_connect()
get_networktime()

#Get curent time from the internet
#standard Micropython does not work on lobo 
#from ntptime import settime
#settime()
