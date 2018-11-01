import machine,time
from machine import Pin, Signal, PWM
#blue led on pin 21
#green = Signal( Pin(18,Pin.OUT) )
#red = Signal( Pin(19,Pin.OUT) )
#blue = Signal( Pin(23,Pin.OUT) )

nobeep=Pin(25, Pin.OUT, value=0 )

def pwmled(pin):
    #all leds use the same timer
    led=PWM(pin,timer=1)
    led.init(freq=10000)
    led.duty(100)
    return led

# Hardware setup 
    
# #connect to Top of M5stack Base 
# grn_pwm=pwmled(18)
# red_pwm=pwmled(19)
# blu_pwm=pwmled(23)

#Connect to left of M5Stack base
grn_pwm=pwmled(2)
red_pwm=pwmled(5)
blu_pwm=pwmled(26)


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


#SENSITIVITY = 1
while 1:
    x,y,z = motion.acceleration
    x1 = min( abs(int( x *10 )),100)
    y1 = min( abs(int( y *10 )),100)
    z1 = min( abs(int( z *10 )),100)
    #print(x1,y1,z1)
    blu_pwm.duty(x1)
    grn_pwm.duty(y1)
    red_pwm.duty(z1)
    time.sleep_ms(100)

    
print('Done')
