# -----------------------
# flashing led
# -----------------------
import time
from machine import Pin

#blue led on pin 2
blue=Pin(2,Pin.OUT);

while True:
    for x in range(20):
        blue.value(0)
        time.sleep_ms(x*10)
        blue.value(1)
        time.sleep_ms(10)

blue.value(0)
print('Done')


