# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:08:31 2016

@author: ericgrimson
"""


epsilon = 0.0001
num_guesses = 0
low = 0
negative = False
print("Pick a cube for a number.", end= ' ')
cube = float(input("We will compute a cube root for: "))

if cube < 0:
    cube = -cube
    negative = True
    
if cube >= 1:
    high = cube
elif cube < 1:
    low = cube
    high = 1
else:
    print("Invalid number. Try another number")
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1

print('num_guesses =', num_guesses)
#To round the guess number to the whole number
if abs(round(guess) - guess) <= epsilon:
    guess = round(guess)
#Add the negative sign back to guess if cube was negative
if negative == True:
    guess = -guess
    cube = -cube
print(guess, 'is close to the cube root of', cube)
