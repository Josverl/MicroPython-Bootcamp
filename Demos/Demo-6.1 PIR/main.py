print("-------------------------------------")
print("Demo 6.1-Passive Infra Red Sensor    ")
print("-------------------------------------")

import windows
tft=windows.tft

windows.borders()
windows.header('Demo 6.1-PIR Sensor ')
windows.mainwindow()

windows.writeln("")
windows.writeln("PIR  connected to Port B\nWhite wire = Pin 26 ")
windows.writeln("")

windows.writeln("Run PIRDisplay.py") 