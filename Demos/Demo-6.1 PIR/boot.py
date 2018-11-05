# This file is executed on every boot (including wake-boot from deepsleep)
#-----------------------------------------------------

# This file is executed on every boot (including wake-boot from deepsleep)
import sys
import machine

# Set default path
# Needed for importing modules and upip
sys.path[1] = '/flash/lib'

def get_networktime():
    my_timezone = "CET-1CEST" # found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
    rtc = machine.RTC()
    rtc.init((2018, 01, 01, 12, 12, 12))
    rtc.ntp_sync(server= "", tz=my_timezone, update_period=3600)

# Auto Connect to the network, starts autoconfig if needed
import wifisetup
#wifisetup.auto_connect()
#get_networktime()

# uncomment for file access functions
# from upysh import *

