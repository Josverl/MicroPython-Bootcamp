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
import m5stack

def beepHappy():
    #Happy 
    m5stack.tone(4200, 80)
    m5stack.tone(2800, 100)
    m5stack.tone(4200, 60)

def beepSad():
    #Sad
    m5stack.tone(1200, duration=100)
    m5stack.tone(700, duration=120)
    m5stack.tone(300, duration=100)

#general init so that we can re-use the tft 
screen_w = const(240)
screen_h = const(320)
header_h = const(32)

if not 'tft' in dir():
    import display
    tft = display.TFT()
    tft.init(tft.M5STACK, width=screen_w, height=screen_h, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1)
    tft.font(tft.FONT_DejaVu18, transparent = False )
    tft.text(0,0,'')

def log(text):
    # Connect to WiFi 
    tft.text(tft.LASTX ,tft.LASTY,text+'\n')


def connectWifi():
    "Connect to WiFi"
    import network, time
    #read network info from : myconfig.py
    try:
        from myconfig import wifi_ssid , wifi_psk
    except:
        print('No Network configuration file found')
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
        beepSad()
        return False

def getNetworkTime(timezone = "CET-1CEST"):
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
    print(rtc.now())


#simplify filesystem access from the prompt
from upysh import *


# Connect to WiFi 
log('Connect to WiFi...')
connected = connectWifi()
if connected:
    log('Get network Time...')
    getNetworkTime()


    
#----------
# Start FTP Server
#-----------
StartFTP = False
if StartFTP:
    log('Start FTP Server...')
    from network import ftp
    ftp.start(user="micro", password="python")
    time.sleep(1)
    _=ftp.status()
    print("FTP server: {}, {} on {}".format(_[2],_[3],_[4]))

log('>main.py')

#Allow the screen to be re-used 
tft.deinit()

 
