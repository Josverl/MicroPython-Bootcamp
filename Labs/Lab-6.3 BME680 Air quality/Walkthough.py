#Lab 6.3 walkthough 
#Only once 
#mkdir('/flash/lib')
from upysh import *

import bme680
from i2c import I2CAdapter
if not 'i2c_bus' in dir():
    i2c_bus = I2CAdapter(sda=21,scl=22)
#Specify the Adafruit non-default address 
sensor = bme680.BME680(i2c_addr=119, i2c_device=i2c_bus)

# These oversampling settings can be tweaked to change sensitivity
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

if sensor.get_sensor_data():
    output = "{} C, {} hPa, {} RH, {} RES,".format(
        sensor.data.temperature,
        sensor.data.pressure,
        sensor.data.humidity,
        sensor.data.gas_resistance)
    print(output)


sensor.get_filter()
