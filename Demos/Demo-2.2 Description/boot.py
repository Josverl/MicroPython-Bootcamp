
#Standard function to connect to the network 
def do_connect():
    import network, time
    #read network info from config  file
    from myconfig import ssid , psk
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, psk)
        #Wait for WiFi connection 
        while not sta_if.isconnected():
            BlinkLed(led)
            print(".", end="")
            time.sleep_ms(200)
    print('network config:', sta_if.ifconfig())

do_connect()
#Get curent time from the internet
from ntptime import settime
settime()