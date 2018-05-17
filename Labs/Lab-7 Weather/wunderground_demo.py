"""
IoT Bootcamp - weatherstation.py 
Marcus Tarquinio, Jos Verlinde
28th Abril 2018
"""

import machine
import time
import bme280
import socket
import ujson

import urequests

PinScl = 15
PinSda = 4
PinDisplay = 16

if not 'i2c' in dir():
    i2c = machine.I2C(scl=machine.Pin(PinScl), sda=machine.Pin(PinSda))

for i in i2c.scan():
    print(hex(i))

if not 'bme' in dir():
    bme = bme280.BME280(i2c=i2c, address=0x76)

def clock():
    print("Clock")

def wunderground():
    #load information for location 
    url = 'http://api.wunderground.com/api/35bb891b4697284b/geolookup/forecast/q/49.53892899,6.12860155.json'
    try: 
        #ask for forecast
        response = urequests.get(url)
        #extract the json , and convert it to a dict in one go
        forecast = response.json()
    except:
        print('Could not retrieve the wether forecast')
    finally:
        response.close() 
    
    forecast['location']['country_name']
    forecast['location']['city']
    #Just one day 
    day=forecast['forecast']['txt_forecast']['forecastday'][0]
    print( day['title'] )
    print( day['fcttext'] )
    print( day['icon'] ,  day['icon_url']  )

    #all days 
    for day in forecast['forecast']['txt_forecast']['forecastday']:
        print( day['title'] )
        print( day['fcttext'] )
        print( day['icon'] ,  day['icon_url']  )

while True:
    print(bme.values)
    time.sleep_ms(1000)
