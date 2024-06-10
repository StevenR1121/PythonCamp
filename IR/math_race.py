"""
Author: Steven Richardson
Updated 6/9/2024

program for circuit playground express board with conjuction of at least two other ir transmitters

the math race reciver will take simple ir outputs and display them on a led strip
the game length is dictated by the number of pixels assiged in num_pixels

two teams compete to finish the math problems provided on by math_transmiter.py script
if correctly answered, an led will update with the teams color

can be used with several transmiters
"""
import board
from rainbowio import colorwheel
import neopixel
import pulseio
import adafruit_irremote

pixel_pin = board.A1
num_pixels = 10 #set game length

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

try:
    pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)# make a ir reader
except AttributeError as err:
    raise NotImplementedError(
        "This example does not work with Circuit Playground Bluefruti!"
    ) from err

# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

RED = (255, 0, 0)# for easy color representations
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

team_A_points = 0# team points
team_B_points = 0

for i in range(num_pixels): # clear leds to start
    pixels[i] = (0,0,0) 
    pixels.show()

while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        continue
    except adafruit_irremote.IRDecodeException:
        # Something got distorted
        continue

    print("Infrared code received: ", received_code)# recive codes
    if received_code == (250, 250, 250, 104):# inverse of transmitted code
        
        print("TEAM A GETS A POINT")
        pixels[team_A_points] = RED
        team_A_points +=1
        pixels.show()
        if team_A_points == num_pixels:
            print(" TEAM A WINS ")
            break
        
    if received_code == (5, 5, 5, 104):
        
        print("TEAM B GETS A POINT")
        team_B_points -=1
        pixels[team_B_points] = GREEN
        pixels.show()
        if team_B_points * -1 == num_pixels-1:
            print(" TEAM B WINS ")
            break
        
        

        
