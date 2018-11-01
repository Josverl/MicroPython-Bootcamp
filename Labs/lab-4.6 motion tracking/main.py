print("-------------------------------------")
print("Lab 4.6 Motion Tracking              ")
print("-------------------------------------")

import machine
import m5stack

#init only one time 
if not 'tft' in dir():
    tft = m5stack.Display()

if not 'i2c' in dir():
    i2c = machine.I2C(0, sda=21, scl=22)


