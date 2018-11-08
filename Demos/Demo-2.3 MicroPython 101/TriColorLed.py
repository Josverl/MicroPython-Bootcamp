# 3 Color Led attached to Port A and B 

# PORT A 
# 21 = white  ==> Blue Led 
# 22 = yellow ==> Red led
# 0v = black  ==> 
# 5v = red    ==> 

# PORT B
# 26 = white  ==> Green Led 
# 36 = yellow ==> 
# 0v = black  ==> 
# 5v = red    ==> 

import time
from machine import Pin, Signal
red  = Signal( Pin(22,Pin.OUT))
blue = Signal( Pin(21,Pin.OUT))
green= Signal( Pin(26,Pin.OUT))


def go_white():
    red.on()
    green.on()
    blue.on()
    return
    
def go_black():
    red.off()
    green.off()
    blue.off()
    return

def go_red():
    red.on()
    green.off()
    blue.off()
    return

def go_blue():
    red.off()
    green.off()
    blue.on()
    return

def go_green():
    red.off()
    green.on()
    blue.off()
    return

def go_orange():
    red.on()
    green.on()
    blue.off()
    return

def go_color(r=0,g=0,b=0):
    red.value(r)
    green.value(g)
    blue.value(b)
    return

go_white()
go_black()
go_red()
go_blue()
go_green()
go_color(1,1,0) #yellow
go_color(1,0,1) #purple
go_color(0,1,1) #lightblue

while True:
    #Cycle though 1 , 2 then all colors 
    for num in range(1,4):
        for r in range(2):
            for g in range(2):
                for b in range(2):
                    if (r+g+b) == num: 
                        go_color(r,g,b)
                        print( r,g,b)
                        time.sleep(1)
    go_black()

print('done')            


