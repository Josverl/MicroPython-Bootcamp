import window
from pause import *
from upysh import *

tft =  window.tft

folder = '/flash/testimages'
files = os.listdir(folder)

ls(folder)
for file in sorted(files,reverse=True):
    tft.clear(tft.BLACK)
    fname= '{}/{}'.format(folder,file)
    tft.image(0, 0, fname )    
    pause(fname)

#placed relative to window

