print("-------------------------------------")
print("Lab 6.3 Air Quality                  ")
print("-------------------------------------")

# import MCU680


# MCU680.t3.stop()
# MCU680.t3.deinit()

import windows
import time

windows.borders()
windows.header('Lab 6.3 Air Quality')
windows.mainwindow()

import timer_display as td

td.start()
