#!/usr/bin/env python
import bme680
from i2c import I2CAdapter
#from mqtt import MQTTClient
import time

def settimeout(duration):
     pass


client = MQTTClient("wipy", "192.168.0.30", port=1883)
client.settimeout = settimeout
client.connect()

i2c_bus = I2CAdapter()
#Specify the Adafruit non-default address 
sensor = bme680.BME680(i2c_addr=119, i2c_device=i2c_bus)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print("Polling:")
try:
    while True:
sensor.data
            #client.publish("test", output)
            time.sleep(1)
except KeyboardInterrupt:
    pass

import sys 
print (sys.platform)
