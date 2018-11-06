print("-------------------------------------")
print("Lab 7 Weather Station                ")
print("-------------------------------------")

import windows
import time
tft=windows.tft

windows.borders()
windows.header('Lab 7 Weather Station')
windows.mainwindow()

windows.writeln("IP : {}".format(wifisetup.wlan_sta.ifconfig()[0] ) )
windows.writeln("Hardware setup:")
windows.writeln("Port B:MCU680 Sensor\nPin 26 & 36")

#windows.writeln("Port A: FAN Module\nPin 21 = White")

exec( open('mystation.py').read() , globals() )