#lab 4.6 motion sensor

import machine,time
if not 'i2c' in dir():
    i2c = machine.I2C(0, sda=21, scl=22)

if 104 in i2c.scan():
    print('motion sensor detected on i2cbus 0')


from mpu9250 import MPU9250
imu = MPU9250(i2c)
print(imu.acceleration)
print(imu.gyro)
print(imu.magnetic)


from fusion import Fusion
fuse = Fusion()

# Choose test to run
Timing = True

if Timing:
    accel = imu.acceleration
    gyro = imu.gyro
    start = time.ticks_us()  # Measure computation time only
    fuse.update_nomag(accel, gyro) # 979μs on Pyboard
    t = time.ticks_diff(time.ticks_us(), start)
    print("Update time (uS):", t)



count = 0

while True:
    fuse.update_nomag(imu.acceleration, imu.gyro)
    if count % 50 == 0:
        print("Heading, Pitch, Roll: {:7.3f} {:7.3f} {:7.3f}".format(fuse.heading, fuse.pitch, fuse.roll))
    time.sleep_ms(20)
    count += 1



'''
This driver is notsupported by the fusion library 

#import mpu9250
from mpu9250 import MPU9250

sensor = MPU9250(i2c_bus)
#help(sensor)

print("MPU9250 id: " + hex(sensor.whoami))

def simple():
    for i in range(20):
        print(sensor.acceleration)
        print(sensor.gyro)
        print(sensor.magnetic)
        time.sleep_ms(1000)


simple()
'''