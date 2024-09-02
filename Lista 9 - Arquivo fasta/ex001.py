#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:24:42 2024

@author: mauricio
"""

arc = open("Corona_genomic.fasta", "r")

desc = arc.readline()

dna = arc.readlines()

info = {"descricao" : desc, "dna" : dna}

dna_compl = ""
for i in info["dna"]:
    if info["dna"] == "A":
        print("a")
        
        
        
