#todo Noise cancelation :-) 
#Speaker = machine.Pin(25, machine.Pin.OUT,machine.Pin.PULL_UP)

import machine 
# Speed 
pwmFan = machine.PWM(machine.Pin(5))
#Direction
reverseFan = machine.Pin(26, machine.Pin.OUT)

#Set Direction
reverseFan.value(0)
#start at high speed 
pwmFan.duty(100)
#Note : if fan does not work , then eith change the wire

pwmFan.duty(90)
#low speeds may not work 
pwmFan.duty(50)

#very low speed stop 
pwmFan.duty(10)

#Set other Direction
reverseFan.value(1)
#Now it works at 10 % 


