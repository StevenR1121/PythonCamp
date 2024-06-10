"""
Additional Author: Steven Richardson
Updated 6/9/2024

the word game is a wheel of fortune style game where players will guess a letter to a random word
picked from a .txt file included with the game. The txt file is limitted by the memory avalable on
the playground express board. both files need to be on the board for the game to work

i utalized LED's as a UI in conjunction with a serial readout. 
"""


import supervisor
import sys
import time
import board
from rainbowio import colorwheel
import neopixel

import random

def rainbow_cycle(wait):## led animations
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def row_flash(color):
    origin_state = []
    for pixel in pixels:
        origin_state.append(pixel)
    
    for i in range(len(picked_word)):
        pixels[i] = color
        time.sleep(.1)
        pixels.show()
    for i in range(len(picked_word)):
        pixels[i] = (0,0,0)
        time.sleep(.1)
        pixels.show()
    for i in range(len(picked_word)):
        pixels[i] = color
        time.sleep(.1)
        pixels.show()
    for i in range(len(picked_word)):
        pixels[i] = (0,0,0)
        time.sleep(.1)
        pixels.show()
        
    for i in range(len(picked_word)):
        pixels[i] = origin_state[i]
        time.sleep(.01)
        pixels.show()

RED = (255, 0, 0)# for ease of color picking
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixel_pin = board.A1# start leds
pixels = neopixel.NeoPixel(pixel_pin, 10, brightness=0.3, auto_write=False) ### controling 10 pixles

for i in range(10): ## clearing leds
    pixels[i] = (0,0,0)
    pixels.show()
    time.sleep(0.01)
          
file = open(r'\250-most-common-words.txt')# read text file with avalable words
word_list = file.read().split()

picked_word = random.choice(word_list)
print('Length of the word is shown by the LEDs')

num_pixels = len(picked_word)
print(len(picked_word))

for i in range(num_pixels): # setting word length with leds
    pixels[i] = YELLOW
    time.sleep(.01)
    pixels.show()
    time.sleep(0.01)

actual_word=['']*len(picked_word)

def guess_word(guess, picked_word):# guess word cycle
    n=0
    guess_amount=0
    guessed=[guess]
    while n != len(picked_word):
        correct_letter=False
        for i in range(len(picked_word)):
            if guess==picked_word[i]:
                correct_letter=True
                actual_word[i]=guess
                pixels[i] = GREEN
                pixels.show()
                n += 1
        if correct_letter:
            row_flash(GREEN)
            print('guess correct!', actual_word)
        else:
            row_flash(RED)
            print('guess wrong!')
        if n<len(picked_word):
            guess=input('guess again:')
            while guess in guessed:
                row_flash(YELLOW)
                print('you guessed already')
                guess=input('guess again:')
            guessed.append(guess)
            guess_amount += 1
    
    return (actual_word, guess_amount)
def input(text):
    print(text)
    while True:
        s = input()
        return s

guess=input('guess a letter:')
(word,guess_amount)=guess_word(guess, picked_word)


joined_word=''.join(word)
rainbow_cycle(.01)
print(f'You won in {guess_amount} trials, the word is {joined_word}!!!' )



        










    
                
                
                
        
           
        

        
        
        
        
        
        