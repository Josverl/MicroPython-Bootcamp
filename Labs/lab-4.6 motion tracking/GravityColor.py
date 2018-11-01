
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
#init only one time 
if not 'tft' in dir():
    tft = m5stack.Display()

import machine,time
if not 'i2c' in dir():
    i2c = machine.I2C(0, sda=21, scl=22)

MOTION_ID = const(104) 
if MOTION_ID in i2c.scan():
    print('motion sensor detected on i2cbus')
    # load motion sensor logic, 
    # two different devices share the same ID, try and retry  
    try:
        from mpu6050 import MPU6050
        imu = MPU6050(i2c, accel_sf=10)
        print("Gyro+Accelerometer/Compass MPU id: " + hex(imu.whoami))
    except:
        from mpu9250 import MPU9250
        imu = MPU9250(i2c) 
    print("Gyro+Accelerometer/Compass {} id: {}".format(imu.__class__.__name__, hex(imu.whoami)))
else:
   print('No motion sensor detected')


SENSITIVITY = 3

#for i in range(1000):
while 1:
    x,y,z = motion.acceleration
    blue.value(abs(x) > SENSITIVITY)
    green.value(abs(y) > SENSITIVITY)
    red.value(abs(z) > SENSITIVITY)
    time.sleep_ms(100)
    
print('Done')
