print("-------------------------------------")
print("Lab 4.6 Motion Tracking              ")
print("-------------------------------------")

import machine
import m5stack

#init only one time 
if not 'tft' in dir():
    tft = m5stack.Display()

#import rollerball2
