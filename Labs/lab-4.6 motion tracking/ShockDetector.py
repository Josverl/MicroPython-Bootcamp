import machine,time
from machine import Pin, Signal, PWM
import m5stack

#blue led on pin 21
#green = Signal( Pin(18,Pin.OUT) )
#red = Signal( Pin(19,Pin.OUT) )
#blue = Signal( Pin(23,Pin.OUT) )

def pwmled(pin):
    #all leds use the same timer
    led=PWM(pin,timer=1)
    led.init(freq=10000)
    led.duty(100)
    return led

grn_pwm=pwmled(18)
red_pwm=pwmled(19)
blu_pwm=pwmled(23)

if not 'i2c' in dir():
    #avoid recreating the same bus 
    i2c = machine.I2C(0, sda=21, scl=22)
if 104 in i2c.scan():
    print('motion sensor detected on i2cbus')

#load sensor logic
from mpu9250 import MPU9250
motion = MPU9250(i2c)

#shock detector

SENSITIVITY = 11
blu_pwm.duty(0);grn_pwm.duty(0);red_pwm.duty(0)
while 1:
    x,y,z = motion.acceleration
    if x > SENSITIVITY or y > SENSITIVITY or z > SENSITIVITY :
        print('TILT')
        m5stack.Beep(1000)
        ## Make Beep 
        ## Send Alert to MQTT 
        ## Send Alert via Microsoft Flow 
        x1 = min( abs(int( x *10 )),100)
        y1 = min( abs(int( y *10 )),100)
        z1 = min( abs(int( z *10 )),100)
        blu_pwm.duty(x1)
        grn_pwm.duty(y1)
        red_pwm.duty(z1)
    time.sleep_ms(100)
    
    
print('Done')
