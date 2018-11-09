windows.header('Lab 6.3 Air Q - Timer')
#Example using a timer 
import machine
from MCU680 import *

#Timer call back function 
#This will be called repeatedly by a timer
def sensor_cb(timer):
    #external inputs / outputs 
    global readings
    while data_ready():
        read_data()
        readings = process_data()
        #output the results to the serial 
        print("Temperature: {Temp:4.1f} C, Humidity: {Humi:2.0f}%, Altitude: {Alt} meters, Pressure: {Pres:7.2f} HPa".format( **readings))
        #print("IAQ Accuracy: {IAQa} , IAQ : {IAQ}, Gas {Gas} Ohm".format( **readings))
    print('')

init_sensor()

#create a timer
t3 = machine.Timer(3)
# call the sensor_cb function every 5 seconds
t3.init(period=5*1000, mode=t3.PERIODIC, callback=sensor_cb)

done= False
if done:
    t3.stop()
    t3.deinit()

