#!/usr/bin/env python3
# coding: utf-8
#Start Documentation:
#Soll: Bootup def(Farbsequenz), def Dauerbetrieb/(evtl. weiß), def(gl)
# Fehler anzeigen(bsp: rot/rot blinken), 
# advanced: Print job status catchen und RGB Farbe anzeigen lassen.
import time, math
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT      = 5      # Number of LED pixels.
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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#Im Startup soll wie bei der @dge Unit eine colorwipe animation laufen, einmal blau dann weiß
def MainWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)  #Funktion rpi_ws281x.color wandelt DEC in BIN  um
        strip.show()
        time.sleep(wait_ms / 1000.0)        

def JobLight(strip):
    strip.setPixelColor(255, 255, 255)# white wipe
    strip.show()
    return
JobLight(strip)


try:
    while True:
            print ('Starten des Pis sowie des Programmes')
            MainWipe(strip, Color(255, 0, 0))  # Red wipe
            MainWipe(strip, Color(0, 255, 0))  # Blue wipe
            MainWipe(strip, Color(0, 0, 255))  # Green wipe
            time.sleep(3)
            JobLight(strip)
            #JobLight(strip, color) Erst benutzen wenn Logik erfüllt ist
            
except KeyboardInterrupt:
    if args.clear:
            MainWipe(strip, Color(0, 0, 0), 10)
