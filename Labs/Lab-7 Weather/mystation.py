#My Station
import time
#----------------------
# Initialisation 
#----------------------
#Init the screen 
#----------------------
from windows import *

borders()
header('My Weatherstation')
mainwindow()
#----------------------
#connect to the sensors 
#----------------------
write('Loading drivers\n')
import bme680
from i2c import I2CAdapter
if not 'i2c_bus' in dir():
    i2c_bus = I2CAdapter(sda=21,scl=22)
#Specify the Adafruit non-default address 
sensor = bme680.BME680(i2c_addr=119, i2c_device=i2c_bus)

# These oversampling settings can be tweaked to
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

#----------------------
#connect to Thingspeak 
#----------------------
write('Connect to Thingspeak\n')

import network,sys
from umqtt.robust import MQTTClient
import utime
import uos
import gc

#create  MQTT clientID based on the mac address 
import machine, binascii
MAC = binascii.hexlify(machine.unique_id()).decode("utf-8")
myMqttClient = "M5Stack_{}".format(MAC)

# connect to Thingspeak MQTT broker
# connection uses unsecure TCP (port 1883)
thingspeakUrl = "mqtt.thingspeak.com"

thingspeakUserId = "josverlinde"                    # EDIT - enter Thingspeak User ID
thingspeakMqttApiKey = "ZWH8LQHCU7L9ETXA"           # EDIT - enter Thingspeak MQTT API Key (Needs to be generated)

#Channel : My Weather Demo 
thingspeakChannelId = "498254"                      # EDIT - enter Thingspeak Channel ID
thingspeakChannelWriteApiKey = "FOU9KYJM6NDHH43F"   # EDIT - enter Thingspeak Write API Key

thingspeakPort = 1883
useSSL = False

client = MQTTClient(client_id=myMqttClient, 
                    server=thingspeakUrl, 
                    user=thingspeakUserId, 
                    password=thingspeakMqttApiKey, 
                    port= thingspeakPort,
                    ssl = useSSL)

status = client.connect()
tsChannel = bytes("channels/{:s}/publish/{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey), 'utf-8')  

if status == 0:
    writeln('Connected OK')
else:    
    writeln('Error !')

#print(tsChannel)

while True:
    #Clean main window
    mainwindow()
    #-------------------
    #read local sensor
    if sensor.get_sensor_data():
        output = "Temp {} C\nPress :{} hPa\nHumidity  {} RH\nPollution {} RES\n".format(
            sensor.data.temperature,
            sensor.data.pressure,
            sensor.data.humidity,
            sensor.data.gas_resistance)
            
        write(output)
        #Send the data to TS 
        sensordata = "field1={:.1f}&field2={:.1f}&field4={:.1f}&field4={:.1f}\n".format(
            sensor.data.temperature,
            sensor.data.pressure,
            sensor.data.humidity,
            sensor.data.gas_resistance)
        client.publish(tsChannel, bytes(sensordata, 'utf-8') ) 
    
    #------------
    #wait for a while
    time.sleep(30)

#----------------------
#load the weather forecast 







