
from machine import Pin, Signal

# Suppose you have an active-high LED on pin 0
led1_pin = Pin(21, Pin.OUT)
# ... and active-low LED on pin 1
led2_pin = Pin(22, Pin.OUT)

# Now to light up both of them using Pin class, you'll need to set
# them to different values
led1_pin.value(1)
led2_pin.value(0)

# Signal class allows to abstract away active-high/active-low
# difference
led_blue = Signal(Pin(21, Pin.OUT), invert=False)
led_green = Signal(Pin(22, Pin.OUT), invert=False)

# Now lighting up them looks the same
led_blue.value(1)
led_green.value(1)

# Even better:
led_blue.on()
led_green.on()

led_blue.off()
led_green.off()

