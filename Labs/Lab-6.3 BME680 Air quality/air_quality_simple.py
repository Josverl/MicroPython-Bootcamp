#!/usr/bin/env python
import bme680
from i2c import I2CAdapter
import time

#import machine;
#machine.loglevel('*',5)

i2c_bus = I2CAdapter(sda=21,scl=22)

i2c_bus.scan()
#i2c_device is actually the I2C bus
sensor = bme680.BME680(i2c_device=i2c_bus)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)


print("Polling:")
try:
    while True:
        if sensor.get_sensor_data():
            output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity,
                sensor.data.gas_resistance)

            print(output)
'''
gas sensor needs a stable heating 
        if sensor.data.heat_stable:
                print("{0},{1} Ohms".format(output, sensor.data.gas_resistance))
        else:
            print(output)
'''            
            
            time.sleep(1)
except KeyboardInterrupt:
    pass
