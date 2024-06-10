# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the adafruit_irremote.mpy library.

THIS EXAMPLE WORKS WITH CIRCUIT PLAYGROUND EXPRESS ONLY.

This example uses the IR transmitter found near the center of the board. Works with another Circuit
Playground Express running the circuitplayground_ir_receive.py example. Press the buttons to light
up the NeoPixels on the RECEIVING Circuit Playground Express!

Additional Author: Steven Richardson
Updated 6/9/2024

using the pre-existing program from adafruit, I added a math game using a circular logic path
the programm will create a random addition problem, if answered correctly, a ir tranmsion will be emited
hopfully being picked up by the math race receiver. along with the game a simple serial ui and led strip ui
was created

"""

import time
import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground import cp
import supervisor
import sys
import random

# Create a 'PulseOut' output, to send infrared signals from the IR transmitter
try:
    pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2**15)
except AttributeError as err:
    # Catch no board.IR_TX pin
    raise NotImplementedError(
        "This example does not work with Circuit Playground Bluefruit!"
    ) from err

# Create an encoder that will take numbers and turn them into NEC IR pulses
encoder = adafruit_irremote.GenericTransmit(
    header=[9500, 4500], one=[550, 550], zero=[550, 1700], trail=0
)
def give_input(text):
        s = input(text)## check with other things about terminal mode maybe word game can be better
        
        try:
            return int(s)
        except:
            return 0

def create_math_problem():
    x = random.randint(0,100)
    y = random.randint(0,100)
    answer = x + y
    guess=give_input(f'{x} + {y} = ')
    if guess != answer:
        for i in range(10):
            cp.pixels[i] = (255,0,0)
            time.sleep(.1)
        for i in range(10):
            cp.pixels[i] = (0,0,0)
            time.sleep(.01)
        create_math_problem()
    else:
        encoder.transmit(pulseout, [250, 250, 250, 46])
        for i in range(10):
            cp.pixels[i] = (0,255,0)
            time.sleep(.1)
        for i in range(10):
            cp.pixels[i] = (0,0,0)
            time.sleep(.01)
        create_math_problem()

create_math_problem()
