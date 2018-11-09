"""
    Render mandelbrot on Odroid Go
    It's for loboris MicroPython port!
    
    Based on code from https://github.com/pypyjs/pypyjs-examples/
"""
import sys
import time

import display
import machine
import micropython
from micropython import const


TFT_WIDTH = const(320)
TFT_HEIGHT = const(240)

def mandelbrot(tft, width, height, left, right, top, bottom, iterations):
    for y in range(height):
        for x in range(width):
            z = complex(0, 0)
            c = complex(left + x * (right - left) / width, top + y * (bottom - top) / height)
            norm = abs(z) ** 2
            for count in range(iterations):
                if norm <= 4:
                    z = z * z + c
                    norm = abs(z * z)
                else:
                    break

            if count <= 4:
                color = tft.DARKGREY
            elif count <= 8:
                color = tft.GREEN
            elif count <= 10:
                color = tft.BLUE
            elif count <= 12:
                color = tft.RED
            elif count <= 15:
                color = tft.YELLOW
            else:
                color = tft.BLACK

            tft.pixel(x, y, color)


def show(tft):
     # https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/machine#machinewdtenable
    start_time = time.time()
    _ = machine.WDT(False)
    mandelbrot(
        tft,
        width=TFT_WIDTH,
        height=TFT_HEIGHT,
        left=const(-2),
        right=0.5,
        top=const(1.25),
        bottom=const(0),
        iterations=const(40),
    )
    _ = machine.WDT(True)
    duration = time.time() - start_time
    print("rendered in %.1f sec." % duration)

