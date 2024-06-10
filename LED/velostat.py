"""
Author: Steven Richardson
Updated 6/9/2024

script to show the use of a velostate and display simple readings with a LED strip
"""

import time
import board
from rainbowio import colorwheel
import neopixel
import analogio


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


pixel_pin = board.A1# led info
num_pixels = 60

velostat_pin = board.A2# velostat 

analog = analogio.AnalogIn(velostat_pin)# start analog access
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)# start led

analog_read = analog.value/2560 # adjust for simple readings

while True:# loop for continued updates to show led change
    if analog_read <25:# adjust number for given analog read
        for i in range(num_pixels):
            pixels[i] = GREEN
            pixels.show()
            time.sleep(.01)
    else:
        for i in range(num_pixels):
            pixels[i] = RED
            pixels.show()
            time.sleep(.01)