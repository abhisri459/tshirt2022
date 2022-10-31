# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:47:58 2021

@author: HP
"""

print("Factorial Calculator!!!")
n=int(input("Enter the number: "))
p=1
for i in range(2,n+1):
    p*=i
print("Factorial of",n,"=",p)