#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:27:13 2022

@author: andy
"""

with open("calculating_expected_offspring.txt") as f:
    population_in = f.read()
    
pop = [int(i) for i in population_in.split()]
dom = 2 * (sum(pop[0:3]) + 0.75 * pop[3] + 0.5 * pop[4])