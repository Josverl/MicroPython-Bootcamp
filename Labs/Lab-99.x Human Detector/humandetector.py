"""
Demo Passive Infra Red Detector 

Connected to Pin 5
"""
from machine import Pin
from time import sleep

pir = Pin(5, Pin.IN)
while True:
   if pir.value():
      print('Human detected')
   sleep(1)