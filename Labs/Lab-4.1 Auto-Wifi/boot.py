# This file is executed on every boot (including wake-boot from deepsleep)
import sys
import gc
import network

# Set default path
# Needed for importing modules and upip
sys.path.append('/flash/lib')
sys.path.append('/flash/sys_lib')

#----------------------------------------------
#setup some additional logging for instruction 
#Set True/False depending on need 
ShowWifi = False
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
    machine.loglevel('*', machine.LOG_INFO)

#----------------------------------------------


# Connect network
import wifisetup
wifisetup.auto_connect()


if False: 
    #force new network connection 
    import wificonfig
    def start():
        wificonfig.webserver_start()
