#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:32:13 2022

@author: andy
"""

import re


def fasta_to_dict(fasta):
    """
    Parameters
    ----------
    fasta : String
        Fasta file read in from Rosalind, each genome is labelled in the form
        of Rosalind_xxxx

    Returns
    -------
    fasta_dict : Dictionary
        Returns a dictionary where the key is the name of the genome and 
        the value is the genome
    """
    fasta_list_no_ws = fasta.replace("\n","")
    genome_list = list(filter(None,re.split(">Rosalind_[0-9]{0,4}",fasta_list_no_ws)))
    genome_names = re.findall("Rosalind_[0-9]{0,4}",fasta_list_no_ws)
    
    fasta_dict = {k:v for k,v in zip(genome_names,genome_list)}
    return fasta_dict

with open("overlap_graphs.txt") as f:
    fasta_in = f.read()
    
genome_dict = fasta_to_dict(fasta_in)

for k1,v1 in genome_dict.items():
    a = v1[-3:]
    tuple_to_compare = [(u,v) for u,v in genome_dict.items() if u != k1]
    for k2,v2 in tuple_to_compare:
        b = v2[:3]
        if a == b:
            print(k1,k2)