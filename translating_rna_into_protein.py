#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:15:10 2022

@author: andy
"""
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))


with open("translating_rna_into_protein.txt") as f:
    rna = f.read()

prot = ""
for i in range(0,len(rna)-3,3):
    prot += codon_table[rna[i:i+3]]

all_prot = prot.split("*")
print(all_prot[0])