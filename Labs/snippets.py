
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

#------------------------------
# String formatting
# https://pyformat.info/#simple
#----------------------------- 

#basic New
'{} {}'.format('one', 'two')
#basic Old
'%s %s' % ('one', 'two')


#print infromation from a dict 
data = {'first': 'Jos', 'last': 'Verlinde'}
print('{first} {last}'.format(**data) )
#or
'{first} {last}'.format(first='Hodor', last='Hodor!')

#Padding and aligning strings
#Align right:
'{:>10}'.format('test')

#Align left:
'{:10}'.format('test')
#or 
'{:<10}'.format('test')

#Padding numbers
#Similar to strings numbers can also be constrained to a specific width.
'{:4d}'.format(42)


#For floating points the padding value represents the length of the complete output. In the example below we want our output to have at least 6 characters with 2 after the decimal point.
'{:6.2f}'.format(3.141592653589793)
#leading zero
'{:06.2f}'.format(3.141592653589793)


#For integer values providing a precision doesn't make much sense and is actually forbidden in the new style (it will result in a ValueError).
'{:04d}'.format(42)

#Signed
'{:+4d}'.format(42)

#Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.
'{: d}'.format((- 23))


#Datetime
New style formatting also allows objects to control their own rendering. This for example allows datetime objects to be formatted inline:
This operation is not available with old-style formatting.

todo: Add Micropython 

#------------------------------
#ESP32 loging handling
#ESP32 log messages can be disabled or enabled with the desired log level.
#------------------------------
# Logging for the individual components or all components can be set.
# The following constants can be used for setting the log level:
# machine.LOG_NONE, machine.LOG_ERROR, machine.LOG_WARN
# machine.LOG_INFO, machine.LOG_DEBUG, machine.LOG_VERBOSE 
# machine.loglevel(component, log_level)
# Set the log level of the component to level log_level
# component is the name of the component as it apears in log messages.

# NOTE: '*' can be used to set the global log level.

import machine
machine.loglevel("wifi", machine.LOG_DEBUG)
machine.loglevel('*', machine.LOG_VERBOSE)
machine.loglevel('[modnetwork]', machine.LOG_DEBUG)
machine.loglevel('wifi', machine.LOG_DEBUG)
machine.loglevel('tcpip_adapter', machine.LOG_DEBUG)
machine.loglevel('event', machine.LOG_INFO)
    

#