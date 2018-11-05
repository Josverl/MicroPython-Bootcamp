print("-------------------------------------")
print("Demo 6.1-Passive Infra Red Sensor    ")
print("-------------------------------------")

import windows
tft=windows.tft

windows.borders()
windows.header('Demo 6.1-PIR Sensor ')
windows.mainwindow()

windows.writeln("Hardware setup:")
windows.writeln("Port B:PIR Sensor\nWhite wire = Pin 26 ")

windows.writeln("See PIRDisplay.py") 