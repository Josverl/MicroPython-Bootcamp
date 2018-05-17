from machine import Pin, Timer

def displayoffcb(timer):
    print("[tcb] timer: {}".format(timer.timernum()))
    if pir.value() == 0:
        print("Turn the display off")
        tft.backlight(0)
    else:
        print("People still around")
        t1.reshoot()

# This is the function to be executed 
# when the PIR sensor first sees movement
def pircb(p):                    
    print('Human detected', p)  
    print('Turn the display on')      
    tft.backlight(1)
    t1.reshoot()
    
pir = Pin(5, Pin.IN)
pir.irq(trigger=Pin.IRQ_RISING, handler=pircb)   # This defines the event
    
t1 = Timer(1)
t1.init(period=5000, mode=t1.ONE_SHOT, callback=displayoffcb)
