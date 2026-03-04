#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 4.6
import numpy as np
from math import sin, cos, tan, log, log10, cosh, sinh, atan, pi    
y = input("Enter a function f(x)=")
a = float(input("the lower bound: "))
b = float(input("the upper bound: "))

n=100000


def Monte_Carlo_integration(y, a, b, n):
    x = np.linspace(a, b, n)
    return (b - a) * np.mean(eval(y))

print( Monte_Carlo_integration(y, a, b, n) )

