# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:07:42 2019

@author: rasim
"""

def f(x):
    return(x**2 - 4*x + 3)

x1 = int(input('başlangıç değeri giriniz: '))    
x2 = int(input('bitiş değeri giriniz: '))

if f(x1)*f(x2) == 0:
    print("girdiğiniz değerlerden birisi kök!")

else:
    while abs(f(x2)-f(x1)) > 0.01:
        x3 = x1 - f(x1)*(x2-x1) / (f(x2)-f(x1))
        x1, x2 = x2, x3
        if f(x1) == f(x2):
            break
    print(x1, x2, f(x1), f(x2))




