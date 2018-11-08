# 3 Color Led attached to Port A
# 21 = white wire  = Blue Led 
# 22 = yellow wire = Red led
# Ground  = Black = -
# +5v = red = Not Connected 

#--------------------------------------------------------------
from machine import Pin, Signal
#use the pins as an output , and give them timple names 
led_blue = Pin(21, Pin.OUT)
led_red = Pin(22, Pin.OUT)

#--------------------------------------------------------------
# Turn On 
led_blue.value(1)

#--------------------------------------------------------------
#Turn Off 
led_blue.value(0)

#--------------------------------------------------------------
# or by using the signal class 
# we can use the simpler on/off syntax 
# this also covers the case where value(0) would turn on the 

led_blue = Signal(Pin(21, Pin.OUT))
led_red = Signal(Pin(22, Pin.OUT))

# Even better:
led_blue.on()
led_red.on()

#--------------------------------------------------------------
led_blue.off()
led_red.off()

