#walkthough 

#Note: Manual step
# upload the m5stack.py module to /flash/lib
import m5stack
import time

#init display (note should be done only once)
import m5stack
if not 'tft' in dir():
    tft = m5stack.Display()

#Clear the display - Orange background
tft.clear(tft.ORANGE)

time.sleep(1)
tft.clearwin(tft.BLUE)



tft.text(0,tft.CENTER,"tadah")


tft.font(tft.FONT_Default, rotate=0)
tft.set_bg(tft.BLUE)
tft.set_bg(tft.BLACK)

tft.text(0,0,"Top Left")
#go one line down 
for n in range(20):
    tft.text(0,tft.LASTY + 10,"Line {}".format(n+1))