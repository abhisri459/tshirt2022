# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:47:58 2021

@author: HP
"""
import random
print("Card Shuffler!!!")
print("You got:")
deck=[0]
for i in range (2,53):
    deck.insert(i-1,i-1)
random.shuffle(deck)
shape=['Spade','Heart','Club','Diamond']
for i in range(5):
    currshape=int(deck[i]/13)
    val=(deck[i]%13)+1
    currcard=''
    if(val>=2 and val<=10):
        currcard=str(val)
    else:
        if(val==1):
            currcard='Ace'
        elif(val==11):
            currcard='Jack'
        elif(val==12):
            currcard='Queen'
        elif(val==13):
            currcard='King'
    print(currcard,'of',shape[currshape])