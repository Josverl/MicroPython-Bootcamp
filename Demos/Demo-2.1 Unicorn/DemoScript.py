# Use FireFox Chrome browser as some of the input controls depend on Chrome :-( 
# Using some highlights from http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html 

#Basic Intro
# Connect to repl 
help()

#Show interactivity
#Simple math 
42 / 7 

#Print 
x = "test "
print( x * 3)

#Tab Completion 
#type pr<Tab>

#Multi-Line commands
# colon - Identation
for counter in range(5):
    print("Hello again" )


#Be carefull with pasting: Use Paste-Mode 

# Ctrl-E , then Paste 
for counter in range(5):
    print("and the answer is ", end = '') #no Newline 
    x = counter * 3 
    print(x)
#After Pasting 
#Ctrl-D (Done)


#Show What Modules are available 
help('modules') 
import math

#Show what functions etc are provided in the math library
help(math)

#Use genric machine module; not the pyboard specific module
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.on()
pin.off()

#Pins Pins and Pins

#When you use machine.Pin(n), n must be the ESP32 GPIO number (GPIOn) entered as integer. 
#The numbers printed on ESP32 board/module (possible prefixed by IO or some other text) coresponds to ESP32 GPIO numbers.
#If only the text is printed on the board (like ADC1), you must consult the board documentation to see to which GPIO it is connected.

# Pin Number 
# Direction > In or Out 
# What happens if there is no Signal 
#   Pull_Up
#   Pull_Down    


# Blinker [uses Pyboard]
import pyb,time 
led = pyb.LED(1)
while True:
  led.toggle()
  time.sleep_ms(100)


# Using the Servo
# Make sure you have the Servo checkbox marked!

import machine
import pyb
# The pyboard has four simple servo connections
servo = pyb.Servo(1)
servo.angle(90, 5000)

#Combined , use the input to control a servo 
import machine
import pyb
import time

# The slider is connected to pin Y4, try adjusting it
y4 = machine.Pin('Y4')

# The pyboard has four simple servo connections
servo = pyb.Servo(1)

servo.angle(90, 50)
adc = pyb.ADC(y4)

while True:
    input = adc.read()
    print(input)
    newAngle = (input/255*180)-90
    servo.angle(int(newAngle), 2000)
    time.sleep(1)

