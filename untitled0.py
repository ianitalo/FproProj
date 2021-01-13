# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:02:43 2021

@author: jeffe
"""

x = "apple01"
y = "apple10"
a = ""
for i in range(min(len(x),len(y))):
    if x[i] == y[i]:
        a = a + x[i]
    else:
        break
print(a)