
# -----------------------
# flashing led
# -----------------------
import time
from machine import Pin

#blue led on pin 2
blue=Pin(21,Pin.OUT);

for x in range(20):
    blue.value(0)
    time.sleep_ms(x*10)
    blue.value(1)
    time.sleep_ms(10)

blue.value(0)

#-----------
# Snippet WiFI
# Start WiFi  
#-----------
import network, time
wifi_ssid='Bootcamp'
wifi_psk='MicroPython'
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
   wlan.active(False)                  # get the interface's IP/netmask/gw/DNS addresses


#----------
# Snippet: Get Network time 
# Lobo Specific 
#-----------
import machine,time
rtc = machine.RTC()
if not rtc.synced():
    my_timezone = "CET-1CEST" # found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
    rtc = machine.RTC()
    rtc.init((2018, 01, 01, 12, 12, 12))
    rtc.ntp_sync(server= "", tz=my_timezone, update_period=3600)
#need to wait a bit 
while not rtc.synced():
  time.sleep_ms(10)
  
print(rtc.now())

#----------
# Snippet: UniqueID 
# retrieve The machines unique ID 
#-----------
import machine, binascii
id_hex = machine.unique_id()
id_b= binascii.hexlify(id_hex)
#optional - decode to string, takes 2x memory
id_s = id_b.decode("utf-8")
print( "Unique ID: {}".format( id_s ) )

# ------------------------
# Scan for accesspoints
# ------------------------
import network;
nic = network.WLAN(network.STA_IF);
_ = nic.active(True)
#networks = nic.scan()
#sort on signal strength 
networks = sorted(nic.scan(), key=lambda x: x[3], reverse=True)

_f = "{0:<32} {2:>8} {3:>8} {4:>8} {5:>8}"

print( _f.format("SSID","bssid","Channel","Signal","Authmode","Hidden") )
for row in networks: 
     print( _f.format( *row ) ) 

del _f

#----------
# Snippet: FTP Server
# Lobo Specific 
#-----------
import network,time
network.ftp.start(user="micro", password="python")

time.sleep(1)
_=network.ftp.status()
print("FTP server: {}, {} on {}".format(_[2],_[3],_[4]))

#----------
# Snippet: Telnet Server
# Lobo Specific 
#-----------
import network,time
network.telnet.start(user="micro", password="python")

time.sleep(1)
_=network.telnet.status()
print("Telnet server: {} on {}".format(_[1],_[2]))


#----------
# Dir / ls 
# uses upysh modules (preloaded in LoBo) 
#-----------

if not 'ls' in dir():
    from upysh import *
ls

