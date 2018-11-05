#pylint: disable=import-error
from machine import Pin, SPI
from input import DigitalInput
import display
import m5stack
#pylint: enable=import-error

#TODO: does not handle multiple initialisations
if not 'tft' in dir():
    tft = m5stack.Display()


tft.image(x, y, file [,scale, type]



    