# Blink LED 
import machine

BlueLED = machine.Pin(26, machine.Pin.OUT)
BlueLED.value(1)

BlueLED.value(0)

while True:
     BlueLED.value(1)
     BlueLED.value(0)

import time
while True:
     BlueLED.value(1)
     time.sleep(0.5)
     BlueLED.value(0)
     time.sleep(0.5)


# PWM
import machine
BlueLED = machine.PWM(machine.Pin(26), freq=1, duty=50)

BlueLED.deinit()

# Fade LED
import time
import machine
BlueLED = machine.PWM(machine.Pin(26), freq=5000)
while True:
    for i in range(100):
       BlueLED.duty(i)
       time.sleep(0.01)
    for i in range(100, 0, -1):
       BlueLED.duty(i)
       time.sleep(0.01)


# Multicolor LED 
import machine

RedLED = machine.PWM(machine.Pin(22))
GreenLED = machine.PWM(machine.Pin(21))
BlueLED = machine.PWM(machine.Pin(26))

RedLED.duty(100*1/5)
GreenLED.duty(100*3/5)
BlueLED.duty(100*4/5)

RedLED.deinit()
GreenLED.deinit()
BlueLED.deinit()


# Rainbow
import time
import machine

def fade(led, begin=0, end=100, step=1):
    for i in range(begin, end, step):
        led.duty(i)
        time.sleep(0.01) 

RedLED = machine.PWM(machine.Pin(22))
GreenLED = machine.PWM(machine.Pin(21))
BlueLED = machine.PWM(machine.Pin(26))

while True:
   fade(GreenLED)                          # Ramp up green
   fade(RedLED, begin=100,end=0,step=-1)   # Ramp down red
   fade(BlueLED)                           # Ramp up blue
   fade(GreenLED, begin=100,end=0,step=-1) # Ramp down green
   fade(RedLED)                            # Ramp up red
   fade(BlueLED, begin=100,end=0,step=-1)  # Ramp down blue


RedLED.deinit()
GreenLED.deinit()
BlueLED.deinit()


# L9110 Fan Motor
import machine
inA = machine.Pin(21, machine.Pin.OUT)
inB = machine.Pin(22, machine.Pin.OUT)

inA.value(0)    
inB.value(1)    # Forward
inB.value(0)    # Stop
inA.value(1)    # Reverse


import machine
pwmFan = machine.PWM(machine.Pin(21))
reverseFan = machine.Pin(22, machine.Pin.OUT)

pwmFan.duty(70)
pwmFan.duty(50)
reverseFan.value(1)

pwmFan.deinit()


# SG90 MicroServo 

import machine
pwmServo = machine.PWM(machine.Pin(26), freq=50, duty=8)

pwmServo.duty(4)
pwmServo.duty(13)


