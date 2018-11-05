import time, machine
from MCU680 import *

#simple way to ensure that we start reading at the beginning of a frame
init_sensor()

while True:
    while data_ready():
        read_data()
        readings = process_data()
        #print(readings)
        #output the results to the serial 
        print("Temperature: {Temp:4.1f} C, Humidity: {Humi:2.0f}%, Altitude: {Alt} meters, Pressure: {Pres:7.2f} HPa".format( **readings))
        #todo: output the results to the the screen
    time.sleep(1)
