#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:08:57 2023

@author: walden
"""

# *****************************
# Backward Induction Algorithm
# *****************************

# Loading packages
import numpy as np
import scipy

# Backward induction algorithm function
def backward_induction(P, r, rterm, discount):

    """
    Inputs:
    P: S x S x T x A array of transition probabilities
    r: S x T x A array of rewards
    rterm: S array of terminal rewards 
    discount: discount factor between 0 and 1
    """""

    """
    Outputs:
        Q: action-value functions
        v: optimal value functions
        pi: optimal policy
    """""

    # Extracting parameters
    S = r.shape[0]  # number of states
    T = r.shape[1]  # number of stages (excluding terminal stage)
    A = r.shape[2]  # number of actions

    # Storing MDP calculations
    Q = np.full((S, T, A), np.nan) # stores action-value functions
    v = np.full((S, T), np.nan) # stores optimal value function values
    pi = np.full((S, T), np.nan) # stores optimal policy

    for t in reversed(range(T)): # number of decision epochs remaining
        for s in range(S): # each state
            for a in range(A): # each action

                # Computing action-value functions
                if t == max(range(T)): # one decision remaining to be made in planning horizon
                    Q[s, t, a] = r[s, t, a] + discount*np.sum([P[t][a][s,ss]*rterm[ss] for ss in range(S)])  # terminal condition
                else:
                    Q[s, t, a] = r[s, t, a] + discount*np.sum([P[t][a][s,ss]*v[ss, (t+1)] for ss in range(S)])  # backward induction

            # Optimal value function and policies
            v[s, t] = np.amax(Q[s, t, :])  # optimal value function at state s and stage t
            pi[s, t] = np.argmax(Q[s, t, :])  # optimal decision rule

    return Q, v, pi

#----------------------------------------
def load_transitions():
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
    
    return P

#----------------------------------------

def load_terminal_rewards():
    rterm = scipy.io.loadmat('/home/walden/Desktop/windowsFiles/Desktop_fixed/Desktop/dartmouth/Fifth Spring/ENGS 177/Project/sixers/compressed_data_generation/terminal_rewards_by_state.mat')
    rterm = rterm.get('r_T')
    return rterm

#---------------------------------------
P = load_transitions()
rterm = load_terminal_rewards()
r = np.zeros([len(rterm),2,7])

## Calculating value functions and policies using backward induction
Q, v, pi = backward_induction(P, r, rterm, discount=1)

np.save('pi.npy',pi)
np.savetxt('pi.txt',pi)
np.save('v.npy',v)
np.save('Q.npy',Q)