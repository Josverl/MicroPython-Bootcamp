#The basics of using the lcd/tft display 
#load the firmware display module
import display
from pause import *

#create a generic tft driver 
tft = display.TFT()

# Initialize the driver with the correct settings 
tft.init(tft.M5STACK, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1,speed=40000000)

# --------------------------------------------------
# Write some text 
tft.font(tft.FONT_DejaVu18, transparent = False )
tft.text(0,0,'Hello Display')

# --------------------------------------------------
# Other fonts

tft.font(tft.FONT_Tooney, transparent = False )
tft.text(0,40,'Hello Display')

# --------------------------------------------------
# Write some text 

tft.font(tft.FONT_Tooney, transparent = False )
tft.text(0,160,'Hello Display',tft.RED)




