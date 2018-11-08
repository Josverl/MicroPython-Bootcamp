#--------------------------------------
# show information on connected network 
#--------------------------------------
import network

wlan = network.WLAN(network.STA_IF)
if wlan.isconnected():
     wlan.active()
     print('wlan config:', wlan.ifconfig())
     print('Active     :', wlan.active())
          
else:
     print('wlan not connected.')
