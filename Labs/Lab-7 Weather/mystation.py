#My Station
import time, gc
import windows

#----------------------
# Initialisation 
#----------------------
import logging
logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__) #in module
log = logging.getLogger('station')

windows.mainwindow()
#----------------------
#connect to the sensors 
#----------------------
log.info('Loading drivers')
import MCU680
from openweathermap import *
#----------------------
INTERVAL = const(60)
# lat = 52.019445
# lng = 4.431991

CityID='2960316'
APIKey='126c5aa86fcedeb3bb3876202a8afc7c'
#----------------------
#Load openweathermap forecast functions
#load the weather forecast 
#----------------------
country, city ,forecast, weather , temp = '?','?','?','?', 0
try:
    log.info('Retrieve the weather forecast')
    #get the weather forecast 
    country, city ,forecast = getforecast(CityID,APIKey)
    log.info("Get reported current weather")
    country, city ,weather, temp = getcurrentweather(CityID,APIKey)
    log.info('Recieved weather and forecast')
except:
    writeln('Error')
    pass
    
#----------------------
#Automatic Display activation 
#----------------------
windows.writeln('TODO: Automatic Display Activation')

#----------------------
# Now continue to poll, send , and update 
# every x seconds
#----------------------
while True:
    log.info('updating...')
    #Clean main window
    windows.mainwindow()
    windows.writeln("Today's observation for \n{}, {}:".format(country,city) )
    windows.writeln('{}C , {}'.format(temp, weather) )

    windows.writeln("Tomorow's forecast : " )
    windows.writeln('{}\n'.format(forecast) )
    #-------------------

    # #read local sensor
    # if sensor.get_sensor_data():
    #     output = "Temp {} C\nPress :{} hPa\nHumidity  {} RH\nPolution {} RES".format(
    #         sensor.data.temperature,
    #         sensor.data.pressure,
    #         sensor.data.humidity,
    #         sensor.data.gas_resistance)
    #     windows.writeln('Data from local sensor:')    
    #     windows.writeln(output)
    #------------
    #clean memory , and wait for a while
    gc.collect()
    time.sleep(INTERVAL)








