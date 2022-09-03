#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:46:16 2022
@author: andy
"""

with open("finding_a_motif_in_dna.txt") as f:
    dna_string = f.read().split()

dna = dna_string[0]
subset = dna_string[1]
set_length = len(dna)
subset_length = len(subset)
pos = []

for i in range(set_length-subset_length+1):
    if dna[i:i+subset_length] == subset:
        pos.append(i+1)
        
print(*pos,sep = " ")