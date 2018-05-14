#Lab 6.3 walkthough 
#Only once 
#mkdir('/flash/lib')
from upysh import *

cd('/flash/lib')
#copy the libraries
cd('/flash')

i2c = I2CAdapter(sda=21,scl=22)
i2c.scan()

#Specify the Adafruit non-default address 
sensor = bme680.BME680(i2c_addr=119, i2c_device=i2c_bus)

if sensor.get_sensor_data():
    output = "{} C, {} hPa, {} RH, {} RES,".format(
        sensor.data.temperature,
        sensor.data.pressure,
        sensor.data.humidity,
        sensor.data.gas_resistance)
    print(output)


sensor.get_filter()
