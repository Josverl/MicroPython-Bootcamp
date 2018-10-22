# walkthough of functionality provided by the Display module 
# reference:  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display 


def pause(Status = None, msg='Press Enter to continue'):
    from sys import stdin
    if Status:
        print(Status)
    print(msg)
    x = stdin.readline()


import time

#init display, direct from Display class to allow help and completion
if not 'tft' in dir():
    import display
    tft = display.TFT()
    tft.init(tft.M5STACK, width=240, height=320, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1)
    x= tft.tft_setspeed(40*1000000) #40 Mhz - best for M5 Display 
#Clear the display - Default background

tft.clear(tft.ORANGE)

pause("Cleared screen with background")


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
pause("create a simple window grid")

borders()
header('empty')
mainwindow()

#==================================================================
#line by line 
# Todo:  line 1 leaves whitespace on top 

pause("Text can be positioned per pixel")

header('Manual counting lines')
mainwindow()
width, height = tft.fontSize()
#go one line down, Calculate the position
for n in range(10):
    tft.text(0,tft.LASTY + height+2 ,"Line {} ...............".format(n+1), color = tft.ORANGE)
    time.sleep(0.5)

#==================================================================
#Show the auto line advance 
# Todo:   line 1 leaves whitespace on top 
pause("There is also a Text 'Cursor' to allow NEWLINE and Appending text")

header('Automatic line advance')
mainwindow()
tft.text(0,0,"Automatic line advance\n\r") 
time.sleep(0.5)

tft.text(tft.LASTX ,tft.LASTY,"as well as cursor >")

pause("Text will continue")

tft.text(tft.LASTX ,tft.LASTY," position")
time.sleep(0.5)

tft.text(tft.LASTX ,tft.LASTY,"\n\r")
#go one line down, cursor position is advanced automatically 
for n in range(10):
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
fname= '/flash/fred.jpg'
tft.image(0, 0, fname )

#appears relative to window, 
tft.image(0, 0, '/flash/arcelormittal.jpg' )
# todo: Clarify that the jpg is larger than the actual screen 


#start position can be outside screen to allow positioning
#scale downsizes the picture,but causes delay 
tft.image(-20, 0, '/flash/arcelormittal.jpg',scale=2 )


#==================================================================
#loading from SD card is slower (Shared SPI)
#mount the SD card
import uos as os
os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
os.mountsd()
ls('/sd')
cp("/flash/fred.jpg", "/sd/fred.jpg")


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

#different clockspeeds for display 
tft.tft_setspeed(10*100000) #10 Mhz 
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )

tft.tft_setspeed(20*000000) #20 Mhz
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )


tft.tft_setspeed(40*1000000) #40 Mhz - best for M5 Display 
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )

#Overclocking 
# Note that this results in a blurred image as the data is sent quicker than the display can recieve/process 
tft.tft_setspeed(80*1000000) 
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )

#60 does not work , next lover is 40 Mhz 
tft.tft_setspeed(60*1000000) 
mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )


#LoBO 
#BUG : Foreground colour set does not work on font
tft.font(tft.FONT_Comic, transparent = True , color=tft.RED)
#BUG foreground / background colors cannot be set
tft.get_bg() 
tft.get_fg() 
tft.set_bg(tft.NAVY) 
tft.set_fg(tft.RED) 


# Read a section of the screen 
# tft.readScreen(x, y, width, height [, buff]) 
# Read the content of the rectangular screen area into buffer.
# If the buffer object buff is not given, the new string object with the screen data wil be returned.
# 3 bytes per pixel are returned (R, G, B).
import gc;gc.collect()

SaveScreen = tft.readScreen(0, 0, 100, 100)

tft.clear(tft.BLACK)

tft.restoreScreen(0, 0, 100, 100,SaveScreen)

#todo: verify if the below issues still appear and report to LoBo 
#Remove text does not position correctly in window
#tft.textClear(0,0,"Automatic line advance")

#some images are not relative to windows, but to screen 
    #BUG: appears relative to screen 
    tft.image(0, 0, '/flash/arcelormittal_s.jpg' )
#Scroll display - Not implemented 

#M5STack module
#does not show help or tab completion for inherited display.TFT 

