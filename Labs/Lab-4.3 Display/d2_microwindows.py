import window
import time
from pause import *
from upysh import *

tft =  window.tft

pause('Show Screen Size')

tft.resetwin() 
tft.clear(tft.NAVY)

#get the screensize 
screen_w, screen_h = tft.screensize()
tft.text(120,int(screen_h/2),"{} by {}".format(*tft.screensize()), color = tft.RED)

time.sleep(2)

#Vertical Ruler
tft.line(10, 0, 10, screen_h)
for y in range(0,screen_h,50):
    tft.line(0, y, 20, y,tft.YELLOW)
    tft.text(25 ,y,"{}".format(y), color = tft.WHITE)

time.sleep(2)
#Horizontal Ruler
tft.line(0, 10, screen_w,10)
for x in range(0,screen_w,50):
    tft.line(x, 0, x, 20, tft.YELLOW)
    tft.text(x,25,"{}".format(x), color = tft.WHITE)

pause()

#==================================================================
pause("create a simple window grid")

window.borders()
window.header('empty')
window.mainwindow()

#==================================================================
#line by line 
# Todo:  line 1 leaves whitespace on top 

pause("Text can be positioned per pixel")

window.header('Manual counting lines')
window.mainwindow()
width, height = tft.fontSize()
#go one line down, Calculate the position
for n in range(10):
    tft.text(0,tft.LASTY + height+2 ,"Line {} ...............".format(n+1), color = tft.ORANGE)
    time.sleep(0.5)

#==================================================================
#Show the auto line advance 
# Todo:   line 1 leaves whitespace on top 
pause("There is also a Text 'Cursor' to allow NEWLINE and Appending text")

window.header('Automatic line advance')
window.mainwindow()
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
pause('simulate bold text')

window.header()
txt = "Bolded text\n\r"
tft.text(1,1,txt,tft.YELLOW)
tft.text(2,2,txt,tft.YELLOW)

#==================================================================
#Add Shadow by writing a shifted shadow first  
#requires font set to transparency 
pause('Add Shadow')

window.header()
txt = "Text with added shadow\r\n"
tft.text(3,3,txt,tft.BLACK)
tft.text(1,1,txt,tft.YELLOW)

#==================================================================
pause('Display image loaded to flash')

window.header('Display image from flash')
window.mainwindow(color=tft.WHITE)

#placed relative to window
fname= '/flash/fred.jpg'
tft.image(0, 0, fname )

pause('Display unscaled JPG')
#appears relative to window, 
tft.image(0, 0, '/flash/arcelormittal.jpg' )
# todo: Clarify that the jpg is larger than the actual screen 

pause('Scale down facter 2 , and shift left')

#start position can be outside screen to allow positioning
#scale downsizes the picture,but causes delay 
tft.image(-20, 0, '/flash/arcelormittal.jpg',scale=2 )



#==================================================================
#loading from SD card is slower (Shared SPI)
#mount the SD card
pause('Notice display from SD Card is much slower due to Shared SPI Bus ( Read / Write)')

import uos as os
os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
os.mountsd()
ls('/sd')
cp("/flash/fred.jpg", "/sd/fred.jpg")

window.header('Image from SDCard')
window.mainwindow(color=tft.WHITE)
tft.image(0, 0, '/sd/fred.jpg' )

#Quick 
pause('Flash = Quick')

window.mainwindow(color=tft.WHITE)
tft.image(0, 0, '/flash/fred.jpg' )



if False:
    #different clockspeeds for display 
    tft.tft_setspeed(10*100000) #10 Mhz 
    window.mainwindow(color=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )

    tft.tft_setspeed(20*000000) #20 Mhz
    window.mainwindow(color=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )

    tft.tft_setspeed(40*1000000) #40 Mhz - best for M5 Display 
    window.mainwindow(color=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )

    #Overclocking 
    # Note that this results in a blurred image as the data is sent quicker than the display can recieve/process 
    tft.tft_setspeed(80*1000000) 
    window.mainwindow(color=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )



# Read a section of the screen 
# tft.readScreen(x, y, width, height [, buff]) 
# Read the content of the rectangular screen area into buffer.
# If the buffer object buff is not given, the new string object with the screen data wil be returned.
# 3 bytes per pixel are returned (R, G, B).
import gc;gc.collect() # clear some memory 

pause('Save a section of the screen')
#Show something
tft.image(0, 0, '/flash/fred.jpg' )

pause('Copy & Clear')
screen_copy = tft.readScreen(0, 0, 100, 100)
tft.clear(tft.BLACK)

pause('Restore')
tft.restoreScreen(0, 0, 100, 100,screencopy)
del(screencopy)

#todo: verify if the below issues still appear and report to LoBo 
# Remove text does not position correctly in window
# tft.textClear(0,0,"Automatic line advance")

# some images are not relative to windows, but to screen 
# BUG: appears relative to screen 
#    tft.image(0, 0, '/flash/arcelormittal_s.jpg' )
#Scroll display - Not implemented 

#M5STack module
#does not show help or tab completion for inherited display.TFT 

if None: 
    #fixme: this specific jpg appears relative to screen, not to window 
    tft.image(0, 0, '/flash/arcelormittal_s.jpg' )

    #LoBO 
    #BUG : Foreground colour set does not work on font
    tft.font(tft.FONT_Comic, transparent = True , color=tft.RED)
    #BUG foreground / background colors cannot be set
    tft.get_bg() 
    tft.get_fg() 
    tft.set_bg(tft.NAVY) 
    tft.set_fg(tft.RED) 

