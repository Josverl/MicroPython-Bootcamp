if 'tft' in dir():
    import machine
    print( "Please reset MCU to avoid init the display in 2 different contexts") 
    machine.reset()

import displaydemos as demo

demo.circleSimple();

demo.circleSimple();

demo.ellipseDemo(sec=4, dofill=True)
demo.fontDemo(sec=5 )

demo.lineDemo(sec=5)
demo.roundrectDemo(sec=3, dofill=True)

#-----------------------------------------------
# re-use tft that is started in anorther module

tft=demo.tft 
demo.header('Polygon',False)
# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display
# tft.poly(x, y, r, sides, thick, [color, fillcolor, rotate]) 
# Draw the polygon with center at (x,y) and radius r, with number of sides sides
# The thicknes of the polygon outline is set by the thick argument
# If fillcolor is given, filled polygon will be drawn.
# If rotate is given, the polygon is rotated by the given angle (0~359)


for s in range(3,12,1):
    for angle in range(0,200,6):
        tft.polygon(160,120, int(angle/2), s, 1, tft.RED, tft.RED,angle )
    for angle in range(120,0,-6):
        tft.polygon(160,120, int(angle/2), s, 1, tft.CYAN, tft.BLUE ,angle )

#------------------------------------------------------------------------------
# Display Mandelbrod set graph https://en.wikipedia.org/wiki/Mandelbrot_set
import mandel
mandel.show(tft)
#Runs About 6 minutes 
