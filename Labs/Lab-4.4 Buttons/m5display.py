"""
helper module to init M5 display 
"""

import display

#todo: guard against initilising multiple times 
tft = display.TFT()
# M5Stack display in the correct orientation
tft.init(tft.ILI9341, width=240, height=320, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1, invrot=3)
tft.orient(tft.LANDSCAPE)
