# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:47:58 2021

@author: HP
"""

print("My Calculator!!!")
print ("Select operation")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")
c=int(input("Enter choice(1/2/3/4): "))
arr=['+','-','*','/']
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a,arr[c-1],b,'= ',end='')
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print((a*b))
else:
    print(a/b)