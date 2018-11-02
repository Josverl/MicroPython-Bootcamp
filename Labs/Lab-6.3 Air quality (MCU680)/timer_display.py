#Example using a timer 
import windows
import machine
from MCU680 import *

windows.header('Lab 6.3 Air Q - Display')

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
    windows.mainwindow()
    windows.writeln("Temperature: {Temp:4.1f} C\nHumidity: {Humi:2.0f}%\nAltitude: {Alt} meters\nPressure: {Pres:7.2f} HPa\nAir Quality : {IAQ}".format( **readings) ,windows.tft.WHITE )


def start():
    global t3
    #Clean main window
    windows.mainwindow()
    windows.writeln('Initializing sensor' )

    init_sensor()

    #create a timer
    s=10
    windows.writeln('Starting {}s update'.format(s) )
    t3 = machine.Timer(3)
    # call the sensor_cb function every 2 seconds
    t3.init(period=s*1000, mode=t3.PERIODIC, callback=sensor_cb)

def stop():
    global t3    
    t3.stop()
    t3.deinit()


if __name__ == "__main__":
    start()