#rolerball

import machine
import utime as time

import m5stack          #Helper functions

MOTION_ID = const(104) 
i2c.scan()

if MOTION_ID in i2c.scan():
    print('motion sensor detected on i2cbus')
    # load motion sensor logic, 
    # two different devices share the same ID, try and retry  
    try:
        from mpu6050 import MPU6050
        motion = MPU6050(i2c, accel_sf=10)
        print("Gyro+Accelerometer/Compass MPU id: " + hex(motion.whoami))
    except:
        from mpu9250 import MPU9250
        motion = MPU9250(i2c)
    
    print("Gyro+Accelerometer/Compass {} id: {}".format(motion.__class__.__name__, hex(motion.whoami)))
   
else:
   print('No motion sensor detected')

while True:
    print("Accell x:{:8.6f} y:{:8.6f} z:{:8.6f}".format(*motion.acceleration) )
    time.sleep_ms(100)

while True:
    print("Gyro x:{:8.6f} y:{:8.6f} z:{:8.6f}".format(*motion.gyro) )
    time.sleep_ms(100)

#print(motion.magnetic) 
