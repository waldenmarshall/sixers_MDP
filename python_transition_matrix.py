#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:38:18 2023

@author: walden
"""

import numpy as np
import scipy

path = '/home/walden/Desktop/windowsFiles/Desktop_fixed/Desktop/dartmouth/Fifth Spring/ENGS 177/Project/sixers/compressed_data_generation/transition_matrices/'

P10 = scipy.io.loadmat(path +'turn1to2/P_t1_a0.mat')
P11 = scipy.io.loadmat(path +'turn1to2/P_t1_a1.mat')
P12 = scipy.io.loadmat(path +'turn1to2/P_t1_a2.mat')
P13 = scipy.io.loadmat(path +'turn1to2/P_t1_a3.mat')
P14 = scipy.io.loadmat(path +'turn1to2/P_t1_a4.mat')
P15 = scipy.io.loadmat(path +'turn1to2/P_t1_a5.mat')
P16 = scipy.io.loadmat(path +'turn1to2/P_t1_a6.mat')

P10 = P10.get('P')
P11 = P11.get('P')
P12 = P12.get('P')
P13 = P13.get('P')
P14 = P14.get('P')
P15 = P15.get('P')
P16 = P16.get('P')

P1 = (P10,P11,P12,P13,P14,P15,P16)

del P10, P11, P12, P13, P14, P15, P16

P20 = scipy.io.loadmat(path +'turn2to3/P_t2_a0.mat')
P21 = scipy.io.loadmat(path +'turn2to3/P_t2_a1.mat')
P22 = scipy.io.loadmat(path +'turn2to3/P_t2_a2.mat')
P23 = scipy.io.loadmat(path +'turn2to3/P_t2_a3.mat')
P24 = scipy.io.loadmat(path +'turn2to3/P_t2_a4.mat')
P25 = scipy.io.loadmat(path +'turn2to3/P_t2_a5.mat')
P26 = scipy.io.loadmat(path +'turn2to3/P_t2_a6.mat')

P20 = P20.get('P')
P21 = P21.get('P')
P22 = P22.get('P')
P23 = P23.get('P')
P24 = P24.get('P')
P25 = P25.get('P')
P26 = P26.get('P')

P2 = (P20,P21,P22,P23,P24,P25,P26)

del P20, P21, P22, P23, P24, P25, P26

P = (P1,P2)

del P1, P2

