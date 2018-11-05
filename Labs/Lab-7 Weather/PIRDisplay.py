from machine import Pin, Timer
from time import sleep_ms

import logging
logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__) #in module
log = logging.getLogger('pir')

#M5Fire - White lead on Port B
PIR_PIN = 26 

demo = 1

if demo==1 :
    pir = Pin(PIR_PIN,Pin.IN)
    while True:​
        if pir.value():​
            print('Human detected')
        else :
            print('.',end='')​
        sleep_ms(500) 

#=================================================================

# This is the function to be executed 
# when the PIR sensor first sees movement
def pir_cb(p):                    
    print('Human detected')
    log.debug( p)  
    log.info('Turn the display on')      
    tft.backlight(1)
    #t1.reshoot()

if demo ==2:
    #M5Fire - White lead on Port B
    # Optional parameters handler and trigger defines the event​
    pir = Pin(PIR_PIN, Pin.IN, handler=pir_cb, trigger=Pin.IRQ_RISING) 
        

#=====================================================================

def pir_cb2(p):                    
    print('Human detected')
    log.debug( p)  
    if p.irqvalue() == p.IRQ_RISING:   
        print('Turn the display on')
        tft.backlight(1)
        #and pause the timer to avoid it turning off
        t1.pause()
    else:
        log.debug('Start timer to turn the display off')
        t1.reshoot()

def displayoffcb(timer):
    log.debug("[tcb] timer: {}".format(timer.timernum()))
    #sanity check as things might have changed ...
    if pir.value() == 0:
        log.info("Turn the display off")
        tft.backlight(0)
    else:
        log.info("People still around")
        t1.reshoot()

if demo ==3:

    pir = Pin(PIR_PIN, Pin.IN, handler=pir_cb2, trigger=Pin.IRQ_ANYEDGE) 
    if not ('t1' in dir()):
        t1 = Timer(1)
    t1.init(period=5000, mode=t1.ONE_SHOT, callback=displayoffcb)
    tft.backlight(1)

