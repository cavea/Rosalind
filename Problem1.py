#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 08:53:36 2022

@author: andy
"""

with open("problem1.txt") as f:
    sequence = f.read().replace("\n","")
    
nt_count = {}
for base in sequence:
    try:
        nt_count[base] += 1
    except:
        nt_count[base] = 1