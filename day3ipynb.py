# -*- coding: utf-8 -*-
"""Day3ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XPZQEP6hUpMvI87SFdjLksyTyEtpj2Qf
"""

# Python Program to print Prime Numbers from 1 to 100
 
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

