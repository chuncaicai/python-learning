# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:21:31 2017

@author: Administrator
"""


import random

print("Welcone to 'Guess My Number'!")
print("/n")
print("I'm thinking of a number between 1 and 100\n")
print("Try to guess it in as few attempts as possible\n")

guess=random.randint(1,100)
guesser=101
i=0
while guesser!=guess:
    guesser=int(input("Take a guess:"))
    if guesser<guess:
        print("lower!\n")
    if guesser>guess:
        print("higer!\n")
    i+=1
print("You guessed it!\n")
print("The number is ",guesser)
print("you take ",i," tries!")
    
