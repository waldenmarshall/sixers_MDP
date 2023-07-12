#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:58:14 2023

@author: walden
"""

import itertools as ittl
import pandas as pd

N=6

states=[]


# create nondecreasing sequences
for L in range(1,7):
    seqs = ittl.combinations_with_replacement(range(1, N+1), L)
    for seq in seqs:
        for i in range(len(seq)):
            seq=list(seq)
            if seq[i] == 1:
                seq[i] = 0
            elif seq[i] == 2:
                seq[i] = 1
            elif seq[i] ==3:
                seq[i] = 2
            seq=tuple(seq)
        states.append(seq)
        
    
# write them row by bow    
with open("states.txt", 'w') as file:
    for row in states:
        s = " ".join(map(str, row))
        file.write(s+'\n')