#!/usr/bin/env python
import bme680
from i2c import I2CAdapter
from mqtt import MQTTClient
import time

def settimeout(duration):
     pass

client = MQTTClient("wipy", "192.168.0.30", port=1883)
client.settimeout = settimeout
client.connect()
mqtt_topic = "bme680"

i2c_dev = I2CAdapter()
sensor = bme680.BME680(i2c_device=i2c_dev)

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
        if sensor.get_sensor_data():

            output = "{} C, {} hPa, {} RH, {} RES,".format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity,
                sensor.data.gas_resistance)

            print(output)
            client.publish(mqtt_topic, output)
            # Publish on individual topics for consistency with rpi repo.
            client.publish('bme680-humidity', str(sensor.data.humidity))
            client.publish('bme680-temperature', str(sensor.data.temperature))
            client.publish('bme680-pressure', str(sensor.data.pressure))
            client.publish('bme680-air_qual', str(sensor.data.gas_resistance))
            time.sleep(5)

except KeyboardInterrupt:
    pass
