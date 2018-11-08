#-----------------------------------------------------
# connect to the network details stored in myconfig 
# if no connection is possible , then re-start as an 
# accesspoint using the same config 
#-----------------------------------------------------
print("-- performing boot --")

def do_connect():
    import network, time
    wlan = network.WLAN(network.STA_IF)
    tmo = 50
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect('IOTBOOTCAMP', 'MicroPython')
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
    print('Could not connect to the WiFI network')

def settime():
    #Get curent time from the internet
    import machine
    rtc = machine.RTC()
    rtc.init((2018, 01, 01, 12, 12, 12))
    rtc.ntp_sync(server= "", tz='CET-1CEST', update_period=3600)

print("-- connect to network")

do_connect()

print("-- connect to network")
settime()

print("-- end of boot.py --")


