# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:00:13 2017

@author: Administrator
"""

import random

print("Welcome to Word Jumble!\n")
correct=word="chuncai"
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print(jumble)
guess=""
while guess!=correct:
    guess=input("Guess:")
print("bingo!\n")