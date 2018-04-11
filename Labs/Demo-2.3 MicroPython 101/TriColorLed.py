
import time
from machine import Pin
red=Pin(19,Pin.OUT)
blue=Pin(21,Pin.OUT)
green=Pin(22,Pin.OUT)


def gowhite():
    red.value(1)
    green.value(1)
    blue.value(1)
    return
    
def goblack():
    red.value(0)
    green.value(0)
    blue.value(0)
    return

def gored():
    red.value(1)
    green.value(0)
    blue.value(0)
    return

def goblue():
    red.value(0)
    green.value(0)
    blue.value(1)
    return

def gogreen():
    red.value(0)
    green.value(1)
    blue.value(0)
    return

def goorange():
    red.value(1)
    green.value(1)
    blue.value(0)
    return

def gocolor(r=0,g=0,b=0):
    red.value(r)
    green.value(g)
    blue.value(b)
    return
'''
gowhite()
goblack()
gored()
goblue()
gogreen()
gocolor(1,1,0) #yellow
gocolor(1,0,1) #purple
gocolor(0,1,1) #lightblue

#Cycle though 1 , 2 then all colors 
for num in range(1,4):
    for r in range(2):
        for g in range(2):
            for b in range(2):
                if (r+g+b) == num: 
                    gocolor(r,g,b)
                    print( r,g,b)
                    time.sleep(1)
'''            
goblack()
print('done')            


