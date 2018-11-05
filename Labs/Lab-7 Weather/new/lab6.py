# Demo 6.1
# PIR

from machine import Pin
from time import sleep
pir = Pin(26, Pin.IN)
while True:
   if pir.value():
      print('Human detected')
   sleep(1)   

# PIR with interrupt (LAB 6.1)

from machine import Pin
import time

def callback(p):               # This is the function to be executed 
   print('Human detected', p)  # when the event happens

# Optional parameters handler and trigger defines the event
pir = Pin(26, Pin.IN, handler=callback, trigger=Pin.IRQ_RISING)


# ---------
# MCU680
# ---------

import machine, time
import logging
import ustruct

if not 'uart' in dir():
    uart = machine.UART(1, tx=26, rx=36, baudrate=9600)

# Variables
measurements = bytearray(20)

def init_sensor():
    # Initialize GY_MCU680 to output all supported data types (0x3F --> '00111111')
    _ = uart.write(b'\xa5\x55\x3f\x39') 
    # Initialize GY_MCU680 in continuous output mode, send the data every x
    _ = uart.write(b'\xa5\x56\x02\xfd')
    #simple way to ensure that we start reading at the beginning of a frame
    uart.flush()

def data_ready():
    try:
        return uart.any() >= 20
    except:
        return False

def read_data():
    global measurements
    if uart.any() >= 20:
        _ = uart.readinto(measurements)        

def process_data():
    global measurements
    global uart

    results = {}

    Temp = measurements[4] << 8 | measurements[5]
    results.update({'Temp' : Temp/100})       
    Humi = measurements[6] << 8 | measurements[7]
    results.update({'Humi' : Humi/100})
    Pres = measurements[8] << 16 | measurements[9] << 8 | measurements[10]
    results.update({'Pres' : Pres/100})        
    IAQa = measurements[11] & int('f0',16) >> 4
    results.update({'IAQa' : IAQa})        
    IAQ = measurements[11] & int('0f',16) << 8 | measurements[12]
    results.update({'IAQ' : IAQ})        
    Gas = measurements[13] << 24 | measurements[14] << 16 | measurements[15] << 8 | measurements[16]
    results.update({'Gas' : Gas})
    Alt = ustruct.unpack_from(">h", measurements,17)[0]
    results.update({'Alt' : Alt})    
    return results

init_sensor()

while True:
    while data_ready():
        read_data()
        readings = process_data()
        #print(readings)
        print(measurements)
        #output the results to the serial 
        print("Temperature: {Temp:4.1f} C, Humidity: {Humi:2.0f}%, Altitude: {Alt} meters, Pressure: {Pres:7.2f} HPa, IAQa: {IAQa}, IAQ: {IAQ}".format( **readings))
    time.sleep(1)