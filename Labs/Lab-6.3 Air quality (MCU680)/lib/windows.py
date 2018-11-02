import display
#general init so that we can re-use the tft 
tft = display.TFT()
screen_w = const(320)
screen_h = const(240)
header_h = const(32)

if not 'debug' in dir():
    debug = False
    
def tftinit(splash=True):
    global tft, screen_w, screen_h, debug
    if not 'tft' in dir():
        tft = display.TFT()
    else:
        #assumes tft is indeed a tft  
        tft.deinit()    

    if debug: print('Initialize tft')
    tft.init(tft.M5STACK, width=screen_w, height=screen_h, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1,speed=60000000,splash=splash)
    tft.font(tft.FONT_DejaVu18, transparent = False )
    tft.text(0,0,'')

#draw borders
def borders(clear=True,bg=tft.BLACK,bd=tft.RED,hd=tft.MAROON):
    tft.resetwin()
    if clear:
        tft.clear(bg)
    #around screen 
    tft.rect(0,0,screen_w, screen_h, bd)
    #border around header
    tft.rect(0,0,screen_w, header_h, bd)
    header(bg=hd)
    
def header(text='',fg=tft.YELLOW,bg=tft.MAROON):
    "draw display header and set header text"
    global debug
    #save window (and pos ?) 
    pos = (100,100)
    try:
        #gets the abs position , not relative to window !
        pos = tft.text_x(), tft.text_y()
        tft.savewin()
        if debug: print('savewin')
    except:
        pass
    #header window
    tft.setwin(1, 1, screen_w-2, header_h-2)
    tft.clearwin(bg)
    tft.font(tft.FONT_Comic, transparent = True )
    tft.text(1,1,text,fg) 
    #restore window
    try:
        tft.restorewin()
        if debug: print('restorewin')
    except:
        pass
    #restore text_cursor pos, recalc relative to main window
    tft.font(tft.FONT_DejaVu18, transparent = True )
    tft.text(pos[0]-1,pos[1]-header_h-1,'')

def mainwindow(clear=True,bg=tft.NAVY):
    #Activate main Window
    tft.setwin(1, header_h+1, screen_w-2, screen_h-2)
    #tft.font(tft.FONT_Minya, transparent = True )
    tft.font(tft.FONT_DejaVu18, transparent = True )
    if clear:
        tft.clearwin(bg)
        tft.text(0,0,'') 

def home():
    tft.text(0,0,"") 

def write(text,*args):
    tft.text(tft.LASTX ,tft.LASTY,text,*args)

def writeln(text,*args):
    tft.text(tft.LASTX ,tft.LASTY,text+'\n',*args)

tftinit()

