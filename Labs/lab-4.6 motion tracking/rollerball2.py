from micropython import const 
import m5stack          #Helper functions

import machine



#init only one time 
if not 'tft' in dir():
    tft = m5stack.Display()


if not 'i2c' in dir():
    i2c = machine.I2C(0, sda=21, scl=22)

def ball_move(x, y):
    global _pos
    
    b_left = const(-80)
    b_top = const(-80)
    b_right = const(80)
    b_bottom = const(80)

    if x > b_right:
        x = b_right
    elif x < b_left:
        x = b_left
    if y > b_bottom:
        y = b_bottom
    elif y < b_top:
        y = b_top
    x += 320-(b_right-b_left)
    y += 240-(b_bottom-b_top)
    if (not x == _pos[0]) or (not y == _pos[1]):
        tft.rect(_pos[0]-11, _pos[1]-11, 22, 22, tft.WHITE, tft.WHITE)  # clean
        tft.circle(x, y, 10, tft.RED, tft.RED)  # draw
        _pos[0] = x
        _pos[1] = y


def gyro_start(obj):
	global _pos
	_pos = [0, 0]

	try:
		from mpu6050 import MPU6050
		obj['motion'] = MPU6050(i2c, accel_sf=10)
	except:
		from mpu9250 import MPU9250
		obj['motion'] = MPU9250(i2c)

	obj['buf'] = [[0, 0] for i in range(0, 6)]
	tft.rect(65, 65, 60, 60, tft.WHITE, tft.WHITE)  # old pic dot clean


def gyro_loop(obj):
    motion = obj['motion']
    buffer = obj['buf']
    val_x = 0
    val_y = 0
    for i in range(0, 4):
        raw = motion.acceleration
        val_x += raw[0]
        val_y += raw[1]
    buffer.pop()
    buffer.insert(0, [int(val_x//4), int(val_y//4)])
    val_x = 0
    val_y = 0
    for i in range(0, 6):
        val_x += buffer[i][0]
        val_y += buffer[i][1]

    ball_move(val_x, -val_y)
    obj['buf'] = buffer


def gyro_end(obj):
    obj = {}


#prewstate.register("PREW_GYRO", MState(start=gyro_start, loop=gyro_loop, end=gyro_end))
#init LCS 

#init only one time 
if not 'tft' in dir():
    tft = m5stack.Display()

#dictionary to share 'objects' between functions
obj={}
tft.clear(tft.WHITE)
gyro_start(obj)

while True:
    gyro_loop(obj)

