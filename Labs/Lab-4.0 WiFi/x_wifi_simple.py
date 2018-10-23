#-----------------------------------------------------
# connect to the network details stored in myconfig 
# if no connection is possible , then re-start as an 
# accesspoint using the same config 
#-----------------------------------------------------

def do_connect():
    import network, time
    #read network info from : myconfig.py
    wifi_ssid=b'IOTBOOTCAMP'
    wifi_psk=b'MicroPython'
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
        print('could not connect to WiFi')  
        wlan.active(False)      

def settime():
    #Get curent time from the internet
    from  sys import platform 
    if platform == 'esp32_LoBo':
        #Micropython settime does not work on lobo
        import machine
        from myconfig import timezone
        my_timezone = timezone # found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
        rtc = machine.RTC()
        rtc.init((2018, 01, 01, 12, 12, 12))
        rtc.ntp_sync(server= "", tz=my_timezone, update_period=3600)
           
    else:
        #generic MicroPython 1.9.3
        from ntptime import settime
        settime()
        

do_connect()
settime()




