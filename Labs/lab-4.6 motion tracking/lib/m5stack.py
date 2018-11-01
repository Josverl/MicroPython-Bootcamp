#
# This file is part of MicroPython M5Stack package
# Copyright (c) 2017-2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-m5stack
#

"""
M5Stack specific constants and classes.
"""

# pylint: disable=import-error
import utime as time
import display
import machine
from uos import sdconfig as uos_sdconfig
from uos import SDMODE_SPI
from input import DigitalInput
from machine import Pin, PWM
from micropython import const
# pylint: enable=import-error

BUTTON_A_PIN = const(39)
BUTTON_B_PIN = const(38)
BUTTON_C_PIN = const(37)

SPEAKER_PIN = const(25)

TFT_LED_PIN = const(32)
TFT_DC_PIN = const(27)
TFT_CS_PIN = const(14)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(33)
TFT_MISO_PIN = const(19)

SD_MODE = SDMODE_SPI
SD_CLK = const(18)
SD_MOSI = const(23)
SD_MISO = const(19)
SD_CS = const(4)

def sdconfig(mode=SD_MODE, clk=SD_CLK, mosi=SD_MOSI, miso=SD_MISO, cs=SD_CS):
        uos_sdconfig(mode, clk, mosi, miso, cs)

def tone(frequency, duration=100, pin=SPEAKER_PIN, volume=1):
    pwm = PWM(pin, duty=volume % 50)
    pwm.freq(frequency)
    time.sleep_ms(duration)
    pwm.deinit()

class ButtonA(DigitalInput):
    def __init__(self, callback=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING):
        pin = Pin(BUTTON_A_PIN, Pin.IN)
        DigitalInput.__init__(self, pin, callback=callback, trigger=trigger)

class ButtonB(DigitalInput):
    def __init__(self, callback=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING):
        pin = Pin(BUTTON_B_PIN, Pin.IN)
        DigitalInput.__init__(self, pin, callback=callback, trigger=trigger)

class ButtonC(DigitalInput):
    def __init__(self, callback=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING):
        pin = Pin(BUTTON_C_PIN, Pin.IN)
        DigitalInput.__init__(self, pin, callback=callback, trigger=trigger)

class Display(object):

    def __init__(self, speed=26000000):
        self.speed = speed
        self.tft = self.create()

    def __getattr__(self, name):
        return getattr(self.tft, name)

    def create(self):
        tft = display.TFT()
        tft.init(
            tft.ILI9341,
            spihost=tft.HSPI,
            width=320,
            height=240,
            mosi=TFT_MOSI_PIN,
            miso=TFT_MISO_PIN,
            clk=TFT_CLK_PIN,
            cs=TFT_CS_PIN,
            dc=TFT_DC_PIN,
            rst_pin=TFT_RST_PIN,
            backl_pin=TFT_LED_PIN,
            backl_on=1,
            speed=self.speed,
            invrot=3,
            bgr=True,
            splash=False
        )

        tft.orient(tft.LANDSCAPE)
        tft.font(tft.FONT_Small, fixedwidth=True)

        return tft

