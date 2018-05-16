"""
Lab 6.1 Passive Infra Red Detector 

Connected to Pin 5
"""

from machine import Pin

# This is the function to be executed 
def cb_motion(p):                  
   print('Human detected', p)  # when the event happens

#This is the pin for the PIR sensor 
pir = Pin(5, Pin.IN)

#
result = pir.irq(trigger=Pin.IRQ_RISING, handler=cb_motion)   



