#My Station
import time, gc
import windows;tft=windows.tft

from machine import Pin, Timer

import micropython
micropython.alloc_emergency_exception_buf(100)
#----------------------
# wiring 
#----------------------
PIR_PIN = 2

#----------------------
# Initialisation 
#----------------------
import logging
logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__) #in module
log = logging.getLogger('station')

#-------------------
windows.mainwindow()
#----------------------
#connect to the sensors 
#----------------------
log.info('Loading drivers')
import MCU680
from openweathermap import *
#----------------------
INTERVAL = const(3) #seconds
KEEP_ON = const(1) #seconds

# List of city ID city.list.json.gz can be downloaded here
# http://bulk.openweathermap.org/sample/
CityID='2960316'
APIKey='126c5aa86fcedeb3bb3876202a8afc7c'

 
#----------------------
#Automatic Display activation 
#----------------------
def pir_cb2(p):                    
    log.debug("Change detected : {}".format(p))  
    if p.irqvalue() == p.IRQ_RISING:   
        log.info('Turn the display on')
        tft.backlight(1)
        #and pause the timer to avoid it turning off
        t1.pause()
    else:
        log.debug('Start timer to turn the display off')
        t1.reshoot()

def displayoffcb(timer):
    log.debug("[tcb] timer: {}".format(timer.timernum()))
    #sanity check as things might have changed ...
    if pir.value() == 0:
        log.info("Turn the display off")
        tft.backlight(0)
    else:
        log.info("People still around")
        t1.reshoot()

#----------------------
# with the M5Fire connections the
# PIR cannot be connected at the same time as the Sensor :<  
#----------------------
if False:
    log.info('Start Automatic Display Activation')
    pir = Pin(PIR_PIN, Pin.IN, handler=pir_cb2, trigger=Pin.IRQ_ANYEDGE) 
    if not ('t1' in dir()):
        t1 = Timer(1)
    t1.init(period=KEEP_ON*1000, mode=t1.ONE_SHOT, callback=displayoffcb)
    tft.backlight(1)


#----------------------
#Timer call back function from the air and temp sensor 
#This will be called repeatedly by a timer
#----------------------
readings={}
def sensor_cb(timer):
    #external inputs / outputs 
    global readings
    while MCU680.data_ready():
        MCU680.read_data()
        readings = MCU680.process_data()
        log.info("Recieved readings from sensor")
        #output the results to the serial 
        print("Temperature: {Temp:4.1f} C, Humidity: {Humi:2.0f}%, Altitude: {Alt} meters, Pressure: {Pres:7.2f} HPa".format( **readings))
        #print("IAQ Accuracy: {IAQa} , IAQ : {IAQ}, Gas {Gas} Ohm".format( **readings))
    print('')

MCU680.init_sensor()

#----------------------
#create a timer to automatically for for the time
t3 = machine.Timer(3)
#----------------------
# call the sensor_cb function every 2 seconds
SENSOR_INTERVAL = const(10)
t3.init(period=SENSOR_INTERVAL*1000, mode=t3.PERIODIC, callback=sensor_cb)


#----------------------
# unitinalized values 
#----------------------
country, city ,forecast, weather , temp = '?','?','?','?', 0
#----------------------
# Now continue to poll, send , and update 
# every x seconds
#----------------------
x=0
while True:
    #Clean main window

    #avoid too frequent getting updates; one in every 10 minutes  
    x+=1
    if x%(int(600/INTERVAL)) ==1:
        windows.mainwindow()    
        log.info('updating...')
        #----------------------
        #Load openweathermap forecast functions
        #----------------------
        
        try:
            windows.writeln('Retrieve the weather forecast')
            #get the weather forecast 
            country, city ,forecast = getforecast(CityID,APIKey)
            windows.writeln("Get reported current weather")
            country, city ,weather, temp = getcurrentweather(CityID,APIKey)
            windows.writeln('Recieved weather and forecast')
        except:
            writeln('Error')
            pass    

    windows.mainwindow()    
    windows.writeln("Today's observation for \n{}, {}:".format(country,city) )
    windows.writeln('{}C , {}'.format(temp, weather) )

    windows.writeln("Tomorow's forecast : " )
    windows.writeln('{}\n'.format(forecast) )

    #-------------------

    if readings != {}:

        windows.writeln("Temperature: {Temp:4.1f} C".format( **readings))
        windows.writeln("Humidity: {Humi:2.0f}%".format( **readings))
        windows.writeln("Pressure: {Pres:7.2f} HPa".format( **readings))

    #------------
    #clean memory , and wait for a while
    gc.collect()
    log.debug('sleeping...')
    time.sleep(INTERVAL)
    log.debug('awake!')








