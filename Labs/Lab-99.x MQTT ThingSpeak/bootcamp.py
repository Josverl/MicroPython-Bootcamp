#helper module for the bootcamp
#based on M5Stack

import m5stack

def beepHappy():
    #Happy 
    m5stack.tone(4200, 80)
    m5stack.tone(2800, 100)
    m5stack.tone(4200, 60)

def beepSad():
    #Sad
    m5stack.tone(1200, duration=100)
    m5stack.tone(700, duration=120)
    m5stack.tone(300, duration=100)

#general init so that we can re-use the tft 
screen_w = const(240)
screen_h = const(320)
header_h = const(32)

if not 'tft' in dir():
    import display
    tft = display.TFT()
    tft.init(tft.M5STACK, width=screen_w, height=screen_h, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1)


#draw borders
def borders(border = tft.RED, bg=tft.NAVY):
    global tft, screen_w, screen_h, header_h
    tft.resetwin()
    tft.clear(bg)
    #around screen 
    tft.rect(0,0,screen_w, screen_h, border)
    #border around header
    tft.rect(0,0,screen_w, header_h, border)
    header()
    
def header(text='',fg=tft.YELLOW,bg=tft.MAROON):
    global tft, screen_w, screen_h, header_h
    #draw header 
    tft.setwin(1, 1, screen_w-2, header_h-2)
    tft.clearwin(bg)
    tft.font(tft.FONT_Comic, transparent = True )
    tft.text(0,0,text,fg) 

def mainwindow(clear=True,bg=tft.BLUE):
    global tft, screen_w, screen_h, header_h
    #Activate main Window
    #print(1, header_h+1, screen_w-2, screen_h-2)
    tft.setwin(1, header_h+1, screen_w-2, screen_h-2)
    #tft.font(tft.FONT_Minya, transparent = True )
    tft.font(tft.FONT_DejaVu18, transparent = True )
    if clear:
        tft.clearwin(bg)
        if color != tft.WHITE:
            tft.text(0,0,'',tft.WHITE) 
        else :
            tft.text(0,0,'',tft.BLACK) 
    