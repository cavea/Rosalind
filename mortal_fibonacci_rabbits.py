#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:47:59 2022

@author: andy
"""
import numpy as np


with open("mortal_fibonacci_rabbits.txt") as f:
    month_string = f.read().replace("\n","").split()
    
month = 50#int(month_string[0])
lifespan = 12#int(month_string[1])
"""
rabbit_new = np.array([1]+[0]*(month-1))

rabbit = [1]*lifespan+[0]*(month-lifespan)
total = np.array([0]*month)
i = 0
next_rabbit_index = [i for i, e in enumerate(rabbit_new) if e != 0][i] #initial starting point
"""
"""
while i <= month:#month :#while loop instead?
    #print("i:",i)
    try:
        next_rabbit_index = [i for i, e in enumerate(rabbit_new) if e != 0][i]
    except:
        break
        
    next_rabbit_count = rabbit_new[next_rabbit_index]
    #print("rabbit_new:",rabbit_new)
    #print("next_rabbit_index:", next_rabbit_index)
    #print("next rabbit count",next_rabbit_count)
    if next_rabbit_index < month - lifespan + 1:
        rabbit_add = [1] * lifespan
        end_zeros = [0] * (month - (lifespan + next_rabbit_index))
    else:
        rabbit_add = [1] * (month - next_rabbit_index)
        end_zeros = []
    rabbit_to_add = [0]*(next_rabbit_index)+rabbit_add+end_zeros
    #print("rabbit_to_add:",np.array(rabbit_to_add))
    total += np.array(rabbit_to_add)*next_rabbit_count
    #print("total:",total)
    i += 1
    for j in range(lifespan - 1):
        try:
            rabbit_new[next_rabbit_index+j+2] += next_rabbit_count
        except:
           None 
    #i += 1
print(total[-1])
"""

#More efficient version:
#total = []
u = [1]+[0]*(lifespan-1)
n_pairs_born = 1
#print(total,u)
total = [(sum(u))]
for i in range(month-1):
    u_new = [sum(np.array(u[1::]))*n_pairs_born] +  [u[i] for i in range(lifespan-1)]
    u = u_new
    total = total + [sum(u)]