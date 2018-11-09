if 'demo' in dir():
    import machine
    print( "Please reset MCU to avoid init the display in 2 different contexts") 
    machine.reset()

#Assumes a SD card is inserted 
from upysh import *
import uos as os
_ = os.sdconfig(os.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
_ = os.mountsd()
cp("/flash/fred.jpg", "/sd/fred.jpg")


import time
from pause import *
from upysh import *
import windows
tft =  windows.tft

pause('Show Screen Size')

tft.resetwin() 
tft.clear(tft.BLACK)
      

#get the screensize 
screen_w, screen_h = tft.screensize()
tft.text(120,int(screen_h/2),"{} by {}".format(*tft.screensize()), color = tft.RED)

time.sleep(0.5)

#Vertical Ruler
tft.line(10, 0, 10, screen_h)
for y in range(0,screen_h,50):
    tft.line(0, y, 20, y,tft.YELLOW)
    tft.text(25 ,y,"{}".format(y), color = tft.WHITE)

time.sleep(0.5)
#Horizontal Ruler
tft.line(0, 10, screen_w,10)
for x in range(0,screen_w,50):
    tft.line(x, 0, x, 20, tft.YELLOW)
    tft.text(x,25,"{}".format(x), color = tft.WHITE)

#==================================================================
pause("create a simple window grid")

windows.borders()
windows.header('<insert Tile here>')
windows.mainwindow()

#==================================================================
#line by line 
# Todo:  line 1 leaves whitespace on top 

pause("Text can be positioned per pixel")

windows.header('Manual positioning lines')
windows.mainwindow()
#left top corner
tft.text(0,0,"Line 1 ...............")
width, height = tft.fontSize()
#go one line down, Calculate the position
for n in range(1,10):
    tft.text(0,tft.LASTY + height+2 ,"Line {} ...............".format(n))
    time.sleep(0.5)

#==================================================================
#Show the auto line advance 
# Todo:   line 1 leaves whitespace on top 
pause("There is also a Text 'Cursor' to allow NEWLINE and Appending text")

windows.header('Automatic line advance')
windows.mainwindow()
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
pause('Display image loaded to flash')

windows.header('Display image from flash')
windows.mainwindow(bg=tft.WHITE)

#placed relative to window
fname= '/flash/fred.jpg'
tft.image(0, 0, fname )

pause('Display unscaled JPG')
#appears relative to window, 
tft.image(0, 0, '/flash/arcelormittal_m5.jpg' )

#==================================================================
#loading from SD card is slower (Shared SPI)
#mount the SD card
pause('Notice display from SD Card is much slower due to Shared SPI Bus ( Read / Write)')

windows.header('Image from SDCard(Slow)')
windows.mainwindow(bg=tft.BLACK)
tft.image(0, 0, '/sd/fred.jpg' )

#Quick 
pause('Flash = Quick')
windows.header('Image from Flash (Fast)')
windows.mainwindow(bg=tft.BLACK)
tft.image(0, 0, '/flash/fred.jpg' )





#------------------------------------------------------------------------------
# Display Mandelbrod set graph https://en.wikipedia.org/wiki/Mandelbrot_set

pause('Close')
windows.header('Mandelbrot set')

import mandel
mandel.show(tft)
#Runs About 6 minutes 


if False:
    #different clockspeeds for display 
    tft.tft_setspeed(10*100000) #10 Mhz 
    windows.mainwindow(bg=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )

    tft.tft_setspeed(20*000000) #20 Mhz
    windows.mainwindow(bg=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )

    tft.tft_setspeed(40*1000000) #40 Mhz - best for M5 Display 
    windows.mainwindow(bg=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )

    #Overclocking 
    # Note that this results in a blurred image as the data is sent quicker than the display can recieve/process 
    tft.tft_setspeed(80*1000000) 
    windows.mainwindow(bg=tft.WHITE)
    tft.image(0, 0, '/flash/fred.jpg' )


print('\r\n>>>\r\n')
