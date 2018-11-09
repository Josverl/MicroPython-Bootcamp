#----------------------------------------------
# Conway's Game of Life
# More programs at UsingPython.com/programs
#----------------------------------------------

import random
import time
import os

#---------------------------------------------------------------------------

def initGrid(cols, rows, array):
    for i in range(rows):
        arrayRow = []
        for j in range(cols):
            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                arrayRow += [-1]
            else:
                ran = random.randint(0,3)
                if ran == 0:
                    arrayRow += [1]
                else:
                    arrayRow += [0]
        array += [arrayRow]

#---------------------------------------------------------------------------
    
def printGen(cols, rows, array, genNo):
    home()
    write("Game of Life -- Generation " + str(genNo + 1))
    
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == -1:
                write(".", end=" ")
            elif array[i][j] == 1:
                write("*", end=" ")
            else:
                write(" ", end=" ")
        write("")

#---------------------------------------------------------------------------

#optimize for speed
def fastprintGen(cols, rows, array, genNo):
    home()
    write("Game of Life -- Generation " + str(genNo + 1))
    
    for i in range(rows):
        line = []
        for j in range(cols):
            if array[i][j] == -1:
                line.append('.')
                #write(".", end=" ")
            elif array[i][j] == 1:
                line.append('*')
                #write("*", end=" ")
            else:
                line.append(' ')
                #write(" ", end=" ")
        write(" ".join(line))
#---------------------------------------------------------------------------

def processNextGen(cols, rows, cur, nxt):
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            nxt[i][j] = processNeighbours(i, j, cur)

#---------------------------------------------------------------------------
      
def processNeighbours(x, y, array):
    nCount = 0
    for j in range(y-1,y+2):
        for i in range(x-1,x+2):
            if not(i == x and j == y):
                if array[i][j] != -1:
                    nCount += array[i][j]
    if array[x][y] == 1 and nCount < 2:
        return 0
    if array[x][y] == 1 and nCount > 3:
        return 0
    if array[x][y] == 0 and nCount == 3:
        return 1
    else:
        return array[x][y]

#---------------------------------------------------------------------------
# Additions for M5Stack Display
import display
#initializes the M5Stack display hardware and establishes a display driver
def initdisplay():
    global tft
    if not 'tft' in dir():
        tft = display.TFT()
    else:
        #assumes tft is indeed a tft  
        tft.deinit()    
    tft.init(tft.M5STACK, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1,speed=40000000)
    tft.font( 7, transparent = False )

#left Top corner
def home():
    tft.text(0,0,"") 

#simple replacement of the print function
def write(text, end='\n'):
    tft.text(tft.LASTX ,tft.LASTY,text+end)

#---------------------------------------------------------------------------
############################################################################
#---------------------------------------------------------------------------

ROWS = 18
COLS = 20
GENERATIONS = 10
DELAY = 0.00

thisGen = []
nextGen = []
initdisplay()
initGrid(COLS, ROWS, thisGen)
initGrid(COLS, ROWS, nextGen)

for gens in range(GENERATIONS):
    #printGen(COLS, ROWS, thisGen, gens)
    fastprintGen(COLS, ROWS, thisGen, gens)
    processNextGen(COLS, ROWS, thisGen, nextGen)
    time.sleep(DELAY)
    thisGen, nextGen = nextGen, thisGen

home()
write("Game of Life -- Finished.                   ")

