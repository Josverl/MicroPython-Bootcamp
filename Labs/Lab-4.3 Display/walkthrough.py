#walkthough 

import time

#init display, direct from Display class to allow help and completion
if not 'tft' in dir():
    import display
    tft = display.TFT()
    tft.init(tft.M5STACK, width=240, height=320, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1)

#Clear the display - Default background

tft.clear(tft.ORANGE)

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

#==================================================================
#line by line 
header('Manual counting lines')
mainwindow()
width, height = tft.fontSize()
#go one line down, Calculate the positin
for n in range(20):
    tft.text(0,tft.LASTY + height+2 ,"Line {} ...............".format(n+1), color = tft.ORANGE)
    time.sleep(0.5)

#==================================================================
#Show the auto line advance 
header('Automatic line advance')
mainwindow()
tft.text(0,0,"Automatic line advance\n\r") 
time.sleep(0.5)

tft.text(tft.LASTX ,tft.LASTY,"as well as cursor")
time.sleep(0.5)
tft.text(tft.LASTX ,tft.LASTY," position")
time.sleep(0.5)

tft.text(tft.LASTX ,tft.LASTY,"\n\r")
#go one line down, cursor position is advanced automatically 
for n in range(20):
    tft.text(tft.LASTX ,tft.LASTY ,"Line {}\n\r".format(n+1), color = tft.ORANGE)
    time.sleep(0.5)

#==================================================================
#Make bold by shifting slightly 
#requires font set to transparency 
header()
txt = "Bolded text\n\r"
tft.text(1,1,txt,tft.YELLOW)
tft.text(2,2,txt,tft.YELLOW)

#==================================================================
#Add Shadow by writing a shifted shadow first  
#requires font set to transparency 
header()
txt = "Text with added shadow\r\n"
tft.text(3,3,txt,tft.BLACK)
tft.text(1,1,txt,tft.YELLOW)

#==================================================================
header('Display image from flash')
mainwindow(color=tft.WHITE)

#placed relative to window
tft.image(0, 0, '/flash/fred.jpg' )

#appears relative to window, 
tft.image(0, 0, '/flash/arcelormittal.jpg' )

#start position can be outside screen to allow positioning
#scale downsizes the picture,but causes delay 
tft.image(-20, 0, '/flash/arcelormittal.jpg',scale=2 )


#==================================================================
#loading from SD card is slower (Shared SPI)
#mount the SD card
import uos as os
os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
os.mountsd()

header('Image from SDCard')
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/sd/fred.jpg' )

#Quick 
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )




#fixme: appears relative to screen 
tft.image(0, 0, '/flash/arcelormittal_s.jpg' )

#==================================================================
#draw Rulers to show the size of the Sreen
#make use of the entire screen , and clear it 
tft.resetwin() 
#get the screensize 
screen_w, screen_h = tft.screensize()

#Vertical Ruler
tft.line(10, 0, 10, screen_h)
for y in range(0,screen_h,50):
    tft.line(0, y, 20, y,tft.YELLOW)
    tft.text(25 ,y,"{}".format(y), color = tft.WHITE)

#Horizontal Ruler
tft.line(0, 10, screen_w,10)
for x in range(0,screen_w,50):
    tft.line(x, 0, x, 20, tft.YELLOW)
    tft.text(x,25,"{}".format(x), color = tft.WHITE)
















#LoBO 
#BUG : Foreground colour set does not work on font
tft.font(tft.FONT_Comic, transparent = True , color=tft.RED)
#BUG foreground / background colors cannot be set
tft.get_bg() 
tft.get_fg() 
tft.set_bg(tft.NAVY) 
tft.set_fg(tft.RED) 

#Remove text does not position correctly in window
#tft.textClear(0,0,"Automatic line advance")

#some images are not relative to windows, but to screen 
    #header('Display image from flash')
    #mainwindow(color=tft.WHITE)
    #tft.setwin(1, 1, screen_w-2, header_h-2)
    tft.setwin(1, 33, 318, 238)

    #placed relative to window
    tft.image(0, 0, '/flash/fred.jpg' )
    #appears relative to screen , scale downsizes the image
    #but that slows down the rendering 
    tft.image(-20, 0, '/flash/arcelormittal.jpg',scale=2 )
        
    #BUG: appears relative to screen 
    tft.image(0, 0, '/flash/arcelormittal_s.jpg' )
    

#Scroll display - Not implemented 

#LOBO POLY not defined ?
tft.poly(tft.CENTER, tft.CENTER, int(width/2), 4, 2, TFT.YELLOW)

#M5STack module
#does not show help or tab completion for inherited display.TFT 

