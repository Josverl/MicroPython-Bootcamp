
import displaydemos as demo
#simple access to tft
tft = demo.tft

tft.clear(tft.WHITE)
demo.circleSimple();

#Increase update speed from default 10 MHz to 40Mhz 
tft.tft_setspeed(40*1000*1000)

tft.clear(tft.WHITE)
demo.circleSimple();

tft.clear(tft.WHITE)
demo.ellipseDemo()

tft.clear(tft.WHITE)
demo.fontDemo()

