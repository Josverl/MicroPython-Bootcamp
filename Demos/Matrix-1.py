

import machine, time
from RGB565RGB import *

#define
np = machine.Neopixel(2, 64, 0)

def rainbow(length = 64, loops=120, delay=1, sat=1.0, bri=0.2):
    for pos in range(0, loops):
        for i in range(1, length+1):
            dHue = 360.0/24*(pos+i);
            hue = dHue % 360;
            np.setHSB(i, hue, sat, bri, 1, False)
        np.show()
        if delay > 0:
            time.sleep_ms(delay)

def blinkRainbow(length = 64,loops=10, delay=250):
    for pos in range(0, loops):
        for i in range(1, length+1 ):
            dHue = 360.0/length*(pos+i);
            hue = dHue % 360;
            np.setHSB(i, hue, 1.0, 0.1, 1, False)
        np.show()
        time.sleep_ms(delay)
        np.clear()
        time.sleep_ms(delay)

        
rainbow(delay=200)    
np.clear()




for px in range(1,65):
    np.set(px, np.OLIVE)
    time.sleep_ms(100)

#scale 0..255 
np.brightness(20,True)

np.set(10,0x0000FF)

blinkRainbow()

D_ROWS = 8
D_COLS = 8 
import framebuf
# FrameBuffer needs 2 bytes for every RGB565 pixel
fbuf = framebuf.FrameBuffer(bytearray(D_ROWS * D_COLS * 2), D_ROWS, D_COLS, framebuf.RGB565)

#10x length
fbuf = framebuf.FrameBuffer(bytearray(D_ROWS * D_COLS *10 * 2), D_ROWS, D_COLS *10, framebuf.RGB565)

#TODO Switch Row / Col 
def ShowMatrix(np,fbuf,c_offset=0):
    #Loop over display pixels
    for r in range (0, D_ROWS):
        for c in range (0, D_COLS): 
            #addressing 1
            color = fbuf.pixel(r,c+c_offset)
            #addressing 2
            #color = fbuf.pixel((D_ROWS-r),(D_COLS-c))
            #pixel num in string
            num = (r + c*D_COLS)
            #workaround for funny addressing bug ?
            if num >0:
                num=num+1
            #get color               
            c2 = RGB565toRGB(color)
            #print('{} x {}={} = {}=>{}'.format(r,c,num, color,hex(c2)))
            #Set pixel
            np.set(num,c2)

np.clear()
np.brightness(50,True)
fbuf.fill(RGBtoRGB565(np.TEAL))
fbuf.text('Hello', 0, 0, RGBtoRGB565(np.RED))
#fbuf.line(0, 0, 0,7, 0xffff)


ShowMatrix(np,fbuf,1)

np.clear()  
np.brightness(30,True)
bg = RGBtoRGB565(np.TEAL)
fg = RGBtoRGB565(np.RED)
for c in ' Hello Word ':
    fbuf.fill(bg)
    fbuf.text(c, 0, 0, fg)
    ShowMatrix(np,fbuf)
    time.sleep(1)

    #Scroll Left
    fbuf.scroll(-1,0)
    fbuf.vline(8,0,8,0) 
    ShowMatrix(np,fbuf)    




Sunset565 = RGBtoRGB565(0x593700)
for x in range(32,128):
    fbuf.fill(0)
    print( x , chr(x))
    fbuf.text(chr(x), 0, 0, Sunset565)
    ShowMatrix(np,fbuf)

    time.sleep_ms(10)

#border
fbuf.fill(0)
fbuf.rect(0, 0, 8,8, Sunset565)
fbuf.rect(1,0,3,8, RGBtoRGB565(np.BLUE))
fbuf.vline(0,5,2,RGBtoRGB565(np.BLUE))
fbuf.vline(4,5,2,RGBtoRGB565(np.BLUE))
ShowMatrix(np,fbuf)    

#Scroll right
fbuf.scroll(1,0)
fbuf.vline(0,0,8,0)
ShowMatrix(np,fbuf)    

