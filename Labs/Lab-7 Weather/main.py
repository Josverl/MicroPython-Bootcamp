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
windows.writeln("Port A:MCU680 Sensor")
windows.writeln("Port B:PIR Sensor\nWhite wire = Pin 26 ")




