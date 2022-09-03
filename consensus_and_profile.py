#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:10:44 2022

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

with open("consensus_and_profile.txt") as f:
    fasta_in = f.read()
    
genome_dict = fasta_to_dict(fasta_in)
genome_length = len(genome_dict[list(genome_dict.keys())[0]])

matrix_dict = {"A":[],"C":[],"G":[],"T":[]}
for i in range(genome_length):
    pos = ""
    for genome in genome_dict:
        pos += genome_dict[genome][i]
    for nt in matrix_dict:
        matrix_dict[nt].append(pos.count(nt))
        
        
common_anc = "".join([max(matrix_dict, key = lambda u: matrix_dict[u][i]) for i in range(genome_length)])

print(common_anc)
print("A:",*matrix_dict["A"],sep=" ")
print("C:",*matrix_dict["C"],sep=" ")
print("G:",*matrix_dict["G"],sep=" ")
print("T:",*matrix_dict["T"],sep=" ")
