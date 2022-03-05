#!/usr/bin/env python3
# coding: utf-8

import time, math
from turtle import color
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT      = 62      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
 
    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

        
#Im Startup soll wie bei der @dge Unit eine colorwipe animation laufen, einmal blau dann weiß
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)  #Funktion rpi_ws281x.color wandelt DEC in BIN  um
        strip.show()
        time.sleep(wait_ms / 1000.0)
        

def snow_sparkle(strip,sparkle_delay=20):
    from random import randint
    pixel= randint(0,strip.numPixels())
    speed_delay=randint(100,1000)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0x10,0x10,0x10))
    strip.show()
    time.sleep(speed_delay/1000.0)
    strip.setPixelColorRGB(pixel, 255,255,255)
    strip.show()
    time.sleep(sparkle_delay/1000.0)
    return                                      #Mit return wiederholt sich die function solange, bis der pi sich ausschaltet

def bouncing_balls(strip,ball_count=4, wait_ms=200):
 
    start_time = time.time()
    ClockTimeSinceLastBounce = [0 for i in range(ball_count)]
    StartHeight=1
 
    for i in range(ball_count):
        ClockTimeSinceLastBounce[i] = time.time()
    
    Height = [0 for i in range(ball_count)]
    Position = [0 for i in range(ball_count)]
    ImpactVelocity = [0 for i in range(ball_count)]
    ImpactVelocityStart= math.sqrt(-2 * -9.81 * 1)
    Dampening = [0 for i in range(ball_count)]
    TimeSinceLastBounce = [0 for i in range(ball_count)]
 
    for i in range(0,ball_count,1):
        last_ClockTimeSinceLastBounce = ClockTimeSinceLastBounce[i]
        ClockTimeSinceLastBounce[i] = time.time() - last_ClockTimeSinceLastBounce
 
        Height[i] = StartHeight
        Position[i] = 0
        ImpactVelocity[i] = math.sqrt(-2 * -9.81 * 1)
        TimeSinceLastBounce[i] = 0
        Dampening[i] = 0.90 - (float(i)/(ball_count**2))
 
    while True:
        for i in range(ball_count):
            TimeSinceLastBounce[i] = time.time() - ClockTimeSinceLastBounce[i]
            Height[i] = 0.5 * (-9.81) * (TimeSinceLastBounce[i]**2) + ImpactVelocity[i] * TimeSinceLastBounce[i]
            if (Height[i] < 0):
                Height[i] = 0
                ImpactVelocity[i] = Dampening[i] * ImpactVelocity[i]
                ClockTimeSinceLastBounce[i] = time.time()
                if (ImpactVelocity[i] < 0.01):
                    ImpactVelocity[i] = ImpactVelocityStart
                                  
            Position[i] = round(Height[i] * (strip.numPixels()-1)/StartHeight)   #Hier wird die relative Höhe auf die absolute Höhe mit der LED Anzahl umgewandelt.
        for i in range(ball_count):
            strip.setPixelColorRGB(Position[i], 0, 0,255)    
        strip.show()
        for i in range(strip.numPixels()):
            strip.setPixelColorRGB(i, 0,0,0)


try:
        while True:
            #Entkommentieren um Programm auszuwählen
            colorWipe(strip, color)
            time.sleep(3)
            #theaterChase(strip)
            #theaterChaseRainbow(strip)
            #pulsing_light(strip)
            snow_sparkle(strip)
            #strobe(strip)
            #bouncing_balls()
except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)