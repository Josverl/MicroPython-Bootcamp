#rolerball

import display
import m5stack

import machine,time
if not 'i2' in dir():
    i2c = machine.I2C(0, sda=21, scl=22)

if 104 in i2c.scan():
    print('motion sensor detected on i2cbus')

#load sensor logic
from mpu9250 import MPU9250
imu = MPU9250(i2c)
#load position abstraction
from fusion import Fusion
fuse = Fusion()


print("MPU9250 id: " + hex(imu.whoami))

#init only one time 
if not 'tft' in dir():
    tft = m5stack.Display()

class Ball:
    "a ball to roll"
    x = 100
    y = 100
    size = 10
    color = tft.RED
    fill = tft.RED
    bg = tft.BLACK      #used to remove
    width=320           #screen boundaries 
    height=240
        
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
        self.remove()
        self.x=x2
        self.y=y2
        self.draw()
        

#new balls please
tft.clear()
b = Ball()
b.size = 10
b.draw()


count = 0
while True:
    fuse.update_nomag(imu.acceleration, imu.gyro)

    b.move(round(fuse.pitch),round(fuse.roll/18))
    if count % 10 == 0:
        print("Pitch, Roll: {:7.3f} {:7.3f}".format(fuse.pitch, fuse.roll))
    time.sleep_ms(200)
    count += 1
