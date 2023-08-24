#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *

from threading import Thread
from engine import *

# simple inquiry example
import bluetooth
import keyboard
import numpy as np

import enquiries
import os

from movingDot import *
from Anim import *
    

# LED strip configuration:
LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



  
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
        
low_rgb = [
  '#000000', '#800000', '#008000', '#808000', '#000080', '#800080', '#008080', '#c0c0c0',
  '#808080', '#ff0000', '#00ff00', '#ffff00', '#0000ff', '#ff00ff', '#00ffff', '#ffffff'
]

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
    

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            #strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


def ThreadDraw(grr):
    while True:
        grr.draw()
        time.sleep(0.016)


def ThreadMenu(eng):
   
    while True:
        #os.system('clear')
        options = ['Solid Colors', 'Animations','Animation2']
        choice = enquiries.choose('Choose one of these options: ', options)
        if choice == 'Animations':
             options = ['Once Right to left speed 50', 'Fixed Blue Block all','theaterChaseRainbow',
                        'rainbowCycle','rainbow','colorWipe']
             choice = enquiries.choose('Choose one of these options: ', options)
             if choice == 'Once Right to left speed 50':
                 eng.addAnim(movingDot(0,50,0,Color(255,0,0),'not'))
             if choice == 'Fixed Blue Block all':
                 eng.addAnim(fixedBlock(50,50,Color(0,255,0)))
             if choice == 'theaterChaseRainbow':
                 eng.startFixedAnimation(Aminamtion('theaterChaseRainbow', 10000))
             if choice == 'colorWipe':
                 eng.startFixedAnimation(Aminamtion('colorWipe', 500))
             if choice == 'rainbow':
                 eng.startFixedAnimation(Aminamtion('rainbow', 500))
             if choice == 'rainbowCycle':
                 eng.startFixedAnimation(Aminamtion('rainbowCycle', 500))
            
        if choice == 'Animation2':
             options = ['Red Anim To Solid', 'Blue Anim To Solid']
             choice = enquiries.choose('Choose one of these options: ', options)
             if choice == 'Red Anim To Solid':
                 eng.animTosolid(10,Color(255,0,0))
               
               
               
               
               
               
        if choice == 'Solid Colors':
            options = low_rgb
            choice = enquiries.choose('Choose one of these options: ', options)
           
            eng.setsolidColor(Color(hex_to_rgb(choice)[0],hex_to_rgb(choice)[1],hex_to_rgb(choice)[2]))

# Main program logic follows:
if __name__ == '__main__':
    
    
    TimeDelta = 0.0166666
    eng = engin(100)
    t1 = Thread(target = ThreadDraw, args=(eng,))
    t2 = Thread(target = ThreadMenu, args=(eng,))
    t2.start()        
    t1.start() 
    
    
    while True:       
        time.sleep(TimeDelta)
        eng.update(TimeDelta)
        
        
    
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
