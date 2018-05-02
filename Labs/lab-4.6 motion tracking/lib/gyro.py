import time
help(imu)
imu.magnetic

def Gyro():
    while 1:
        g=imu.gyro
        " {:1} {:1} {:1}".format(g[0],g[1],g[2])
        time.sleep(0.1)

def Compass():
while 1:
        g=imu.magnetic
        " {:1} {:1} {:1}".format(g[0],g[1],g[2])
        time.sleep(0.1)

while 1:
    fuse.update_nomag(imu.acceleration, imu.gyro)
    print('fuse {:1} {:1} '.format(fuse.pitch,fuse.roll))
    time.sleep(0.1)    

    