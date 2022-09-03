#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:02:38 2022

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

with open("finding_a_shared_motif.txt") as f:
    fasta_in = f.read()
genome_dict = fasta_to_dict(fasta_in)

genome_ref_key = list(genome_dict.keys())[0]
genome_ref_value = genome_dict[genome_ref_key]
genome_no_ref = {k:v for k,v in genome_dict.items() if k != genome_ref_key}

common_string_bool = True
i = 0
j = 1
largest_common_string = ""
while (i + j) < len(genome_ref_value):
    common_string_bool = True
    while common_string_bool:
        genome_string = genome_ref_value[i:i+j]
        common_string_bool = all([genome_string in genome_no_ref[gen] for gen in genome_no_ref])
        if common_string_bool:
            largest_common_string = genome_string
            j += 1
            #print(largest_common_string)
    i += 1
        