#walkthough 

import time

#init display, direct from Display class to allow help and completion
if not 'tft' in dir():
    import display
    tft = display.TFT()
    tft.init(tft.M5STACK, width=240, height=320, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1)

#Clear the display - Default background

tft.clear(tft.NAVY)

# fonts used in this demo
fontnames = (
    tft.FONT_Default,
    tft.FONT_7seg,
    tft.FONT_Ubuntu,
    tft.FONT_Comic,
    tft.FONT_Tooney,
    tft.FONT_Minya
)


#general init 
screen_w, screen_h = tft.screensize()
header_h = 32

#draw borders
def borders():
    tft.resetwin()
    tft.clear(tft.NAVY)
    #around screen 
    tft.rect(0,0,screen_w, screen_h, tft.RED)
    #border around header
    tft.rect(0,0,screen_w, header_h, tft.RED)
    header()
    
def header(text=''):
    #draw header 
    tft.setwin(1, 1, screen_w-2, header_h-2)
    tft.clearwin(tft.MAROON)
    tft.font(tft.FONT_Comic, transparent = True )
    tft.text(0,0,text,tft.YELLOW) 

def mainwindow(clear=True,color=tft.BLUE):
    #Activate main Window
    #print(1, header_h+1, screen_w-2, screen_h-2)
    tft.setwin(1, header_h+1, screen_w-2, screen_h-2)
    #tft.font(tft.FONT_Minya, transparent = True )
    tft.font(tft.FONT_DejaVu18, transparent = True )
    if clear:
        tft.clearwin(color)
        if color != tft.WHITE:
            tft.text(0,0,'',tft.WHITE) 
        else :
            tft.text(0,0,'',tft.BLACK) 
            
#==================================================================

borders()
header('empty')
mainwindow()

import micropython
import gc


for n in range(50):
    #micropython.mem_info()
    print("RUNNING")
    exec(open('satimage.py').read(),globals())
    #micropython.mem_info()
    #print("cleaning")
    gc.collect()
    micropython.mem_info()
    print(n, 'Waiting...')
    time.sleep(60*10)
