#rolerball 1 - using Accelerometer

from micropython import const
import display
import m5stack
import time

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


class Ball:
    "a ball to roll"
    size = 10
    color = tft.RED
    fill = tft.RED
    bg = tft.BLACK      #used to remove
    width=320           #screen boundaries 
    height=240
    x = int(width/2)
    y = int(height/2)
            
    def __init__(self, ):
        pass
        
    def draw(self):
        tft.circle(self.x,self.y,self.size,self.color,self.fill)

    def remove(self):
        tft.circle(self.x,self.y,self.size,self.bg,self.bg)

    def move(self, horizontal=0, vertical=0):
        x2 = self.x + horizontal
        x2 = max( x2, self.size) # do not go off the left 
        x2 = min( x2, self.width-self.size)

        y2 = self.y + vertical
        y2 = max( y2, self.size) # do not go off the top 
        y2 = min( y2, self.height-self.size)
        #todo only redraw when needed
        if not ( (self.x == x2) and (self.y == y2)):
            self.remove()
            self.x=x2
            self.y=y2
            self.draw()
        
imu.acceleration

#new balls please
tft.clear()
b = Ball()
b.draw()

count = 0
ACCEL = 10
while True:
    x,y,z = imu.acceleration
    x2 = round(x*ACCEL*-1) #adjust for screen addressing
    y2 = round(y*ACCEL)
    b.move(x2,y2)
    if count % 10 == 0:
        print("x, y: {:7.3f} {:7.3f}".format(x,y) )
    time.sleep_ms(200)
    count += 1

