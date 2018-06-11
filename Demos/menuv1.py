import os
import logging
import m5stack
import windows 
from time import sleep_ms

logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__) #in module
log = logging.getLogger('menu')

#Main Menu 
class Startmenu:
    "Simple menu to start scripts"
    
    def __init__(self):
        #if scripts is None: 
        #all the files ending in .py in the current folder 

        self.cursor = 0
        self.c_old = -1
        self.min = 0
        self.max = 0
        self.maxlines = 9
        self.scripts = None
        self.bg = tft.NAVY
        self.fg = tft.WHITE
        self.cc = tft.YELLOW
        self.selected = None
        self.scripts = [elem for elem in os.listdir('.') if elem.endswith('.py')]
        #todo: sort 
        self.max = min ( len(self.scripts), self.maxlines-1)
        print('max',self.max)
        if self.max >0 : 
            self.min = 1
            self.cur = 1
            
    #note that for up/down the curor is decreased/increased
    def _down_handler(self, pin, pressed):
        if pressed is True:
            log.debug("Down pressed {} {}".format(self.cursor , self.max) )
            if self.cursor <= self.max :
               self.cursor+=1
               self._draw_cursor() 

    def _up_handler(self, pin, pressed):
        if pressed is True:
            log.debug("Up pressed")
            if self.cursor >= self.min:
               self.cursor-=1
               self._draw_cursor() 

    def _select_handler(self, pin, pressed):
        if pressed is True:
            log.info("Select pressed on {} : {}".format(self.cursor,self.scripts[self.cursor]))
            self.selected = self.scripts[self.cursor]
            c = self.cursor
            width, height = tft.fontSize()
            tft.text( 8,c * height+2 ,"{:2} {}".format(c+1,self.selected), color = self.cc)
            
                
    def draw_all(self):
        borders()
        header('Main Menu')
        self.draw_main()
        self._draw_cursor()
        
    def draw_main(self):
        mainwindow(True,self.bg)
        width, height = tft.fontSize()
        #draw page starting at 0
        c = 0
        for fname in self.scripts:
            tft.text( 8,c * height+2 ,"{:2} {}".format(c+1,fname), color = self.fg)
            c+=1
            if c>self.maxlines:
                break
        # if > 10 stop 

    def _draw_cursor(self):
        log.debug("{}".format(self.cursor))
        width, height = tft.fontSize()
        #remove previous cursor
        if self.c_old >-1:
            c = self.c_old
            tft.triangle(2, c*height,2,(c+1)*height,12, c*height+(height>>1), self.bg,self.bg )
           
        #show Cursor 
        c = self.cursor
        tft.triangle(2, c*height,2,(c+1)*height,12, c*height+(height>>1), self.cc,self.cc )
        self.c_old = self.cursor

    def show(self):
        a = m5stack.ButtonA(callback=self._up_handler)
        b = m5stack.ButtonB(callback=self._select_handler)
        c = m5stack.ButtonC(callback=self._down_handler)
        self.draw_all()
        while self.selected is None:
            sleep_ms(50)
        a.deinit()
        b.deinit()
        c.deinit()
        return self.selected
            
m = Startmenu()
script = m.show()
import gc;gc.collect();
exec(open(script).read(),globals());

"""

help(m5stack)
help(m)

self = m
mainwindow()
c = 0
for fname in self.scripts:
    tft.text(0,c * height+2 ,"{:2} {}".format(c,fname), color = tft.ORANGE)
    c+=1

    
x = None 
if x is None:
    print('nope') 


import os
os.listdir('.')
'two.py'.endswith('.py')

#all the files ending in .py in the current folder 
scripts = [elem for elem in os.listdir('.') if elem.endswith('.py')]

help(scripts)


li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]
"""
