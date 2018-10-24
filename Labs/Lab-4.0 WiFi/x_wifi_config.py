#-----------------------------------------------------
# connect to the network details stored in myconfig 
# if no connection is possible , then re-start as an 
# accesspoint using the same config 
#-----------------------------------------------------

def do_connect():
    import network, time
    #read network info from : myconfig.py
    from myconfig import wifi_ssid , wifi_psk
    wlan = network.WLAN(network.STA_IF)
    tmo = 50
    if not wlan.isconnected():
        print('connecting to network...')
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
    else: 
        print('start AccessPoint')  
        wlan.active(False)      
        ap = network.WLAN(network.AP_IF)  # create access-point interface
        ap.active(True)                   # activate the interface
        ap.config(essid=wifi_ssid)         # set the ESSID of the access point
        # Set the authentication mode and password
        ap.config(authmode=network.AUTH_WPA_PSK, password=wifi_psk)

def settime():
    #Get curent time from the internet
    #generic Micropython settime does not work on lobo 
    #from ntptime import settime
    #settime()
    import machine
    from myconfig import timezone
    my_timezone = timezone # found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
    rtc = machine.RTC()
    #Set the system time and date.
    rtc.init((2018, 01, 01, 12, 12, 12))
    #configure to sync the time every hour with a Network Time Protocol (NTP) server
    rtc.ntp_sync(server= "", tz=my_timezone, update_period=3600)

do_connect()
settime()




