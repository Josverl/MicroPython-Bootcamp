#Get curent time from the internet
#Note : The Loboris firmware works different from standard Micropython 
# reference : https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/rtc
from machine import RTC
import time
# Timezone is found in second field, text before the coma, in https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/blob/master/MicroPython_BUILD/components/micropython/docs/zones.csv
timezone = 'CET-1CEST'
rtc = RTC()
#Set the system time and date, (in this case very roughly).
rtc.init((2018, 01, 01, 12, 12, 12))
#configure to sync the time every hour with a Network Time Protocol (NTP) server
rtc.ntp_sync(server= "", tz=timezone, update_period=3600)

# I may take some time for the ntp server to reply, so we need to wait 
# Wait 5 sec or until time is synched ?
tmo = 50
while not rtc.synced():
    utime.sleep_ms(100)
    tmo -= 1
    if tmo == 0:
        break
#get the current,synchonized, time 
rtc.now()
