
import machine,time
from machine import Pin, Signal
#blue led on pin 21
green = Signal( Pin(17,Pin.OUT) )
red = Signal( Pin(5,Pin.OUT) )
blue = Signal( Pin(2,Pin.OUT) )

red.off();blue.off();green.off()
red.on();
blue.on();
green.on()

green

if not 'i2c' in dir():
    i2c = machine.I2C(0, sda=21, scl=22)
if 104 in i2c.scan():
    print('motion sensor detected on i2cbus')

#load sensor logic
from mpu9250 import MPU9250
motion = MPU9250(i2c)


SENSITIVITY = 3

#for i in range(1000):
while 1:
    x,y,z = motion.acceleration
    blue.value(abs(x) > SENSITIVITY)
    green.value(abs(y) > SENSITIVITY)
    red.value(abs(z) > SENSITIVITY)
    time.sleep_ms(100)
    
print('Done')
