#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:43:17 2022

@author: andy
"""

with open("complementing_a_strand_of_dna.txt") as f:
    dna_seq = f.read().replace("\n","")
    
rev_seq = dna_seq[::-1]

comp_seq_AG = rev_seq.replace("A","%tempA%").replace("T","%tempT%")
comp_seq_CT = comp_seq_AG.replace("C","%tempC%").replace("G","%tempG%")

comp_seq_GA = comp_seq_CT.replace("%tempA%","T").replace("%tempT%","A")
comp_seq = comp_seq_GA.replace("%tempC%","G").replace("%tempG%","C")
