import machine
import time 
#to improve error reporting during callbacks 
import micropython
micropython.alloc_emergency_exception_buf(100)

np=machine.Neopixel(15, 24)

#simple Blocking 
# while True:
#     # Set color for pixel 0 (pure red)
#     for n in range(1,10):
#         np.set(n,neo.GREEN)
#         time.sleep(0.1)
#     for n in range(1,10):
#         np.set(n,neo.MAGENTA)
#         time.sleep(0.1)

#global vars 
pos = 0
sat = 1.0
bri = 0.2
loops = 120
t3 = machine.Timer(3)

def rainbow_cb(timer):
    global sat, bri, pos, loops
    pos +=1
    if pos >= loops: 
        pos = 0 
    for i in range(1, 11):
        dHue = 360.0/24*(pos-i)
        hue = dHue % 360
        np.setHSB(i, hue, sat, bri, 1, False)
    np.show()

# call the rainbow_cb function every x mseconds
t3.init(period=150, mode=t3.PERIODIC, callback=rainbow_cb)

#slow down, save power ;-> 
machine.freq(80)


