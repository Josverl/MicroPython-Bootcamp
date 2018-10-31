# This file is executed on every boot (including wake-boot from deepsleep)
import sys
import gc
import network

# Set default path
# Needed for importing modules and upip
sys.path[1] = '/flash/lib'

#----------------------------------------------
#setup some additional logging for instruction 
#Set True/False depending on need 
ShowWifi = True
ShowDebug = False

def wifi_cb(info):
    _red = "\033[31m"
    _cyan= "\033[36m"
    _norm = "\033[00m"
    if (info[2]):
        msg = ", info: {}".format(info[2])
    else:
        msg = ""
    print("\n"+_cyan+"I [WiFi] event: {} ({}){}".format( info[0], info[1], msg)+_norm)

if ShowWifi:
    # Enable  (if supported) 
    try:
        network.WLANcallback(wifi_cb)                    
    except:
        pass

if ShowDebug:
    #enable system wide verbose information messages 
    import machine 
    machine.loglevel('*', machine.LOG_VERBOSE)
    machine.loglevel('[modnetwork]', machine.LOG_DEBUG)
    machine.loglevel('wifi', machine.LOG_DEBUG)
    machine.loglevel('tcpip_adapter', machine.LOG_DEBUG)
    machine.loglevel('event', machine.LOG_DEBUG)
    

#----------------------------------------------

# Auto Connect to the network, starts autoconfig if needed
import wifisetup
wifisetup.auto_connect()

#Note this section is not normally run, 
# but is provided as an example of how to force the autoconfiguration  
if False: 
    #force new network connection 
    import wificonfig
    wificonfig.webserver_start()
