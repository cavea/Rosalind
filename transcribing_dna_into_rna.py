#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:27:33 2022

@author: andy
"""

with open("transcribing_dna_into_rna.txt") as f:
    dna_sequence = f.read().replace("\n","")
    
rna_sequence = dna_sequence.replace("T","U")