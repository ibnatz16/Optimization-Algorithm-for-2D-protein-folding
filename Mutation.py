from Debug import *
from Matrix import *
import random
import sys
import math

directions = ["L", "R", "F"]

def getDir(seq):
    x = random.randint(0,2)
    if directions[x] == seq:
        return getDir(seq)
    return directions[x]

def mutate(pop,prob, len_seq):
    mut_pop=[]
    p = 0
    while p < len(pop):
        seq=pop[p]
        # get random protein to switch
        x = random.randint(0, 2) 
        sequence=[]
       
        for i in range(len(seq)):
            rand= random.random()
            if(rand<=prob):
                nex = getDir(seq[i])
                sequence.append(nex)
                # else:
                # delete do nothing        
            else:
                sequence.append(seq[i])
        if DEBUG_3:
            print('Paramater len', len_seq, 'Seq length', len(sequence))
            print('mutation matrix ', len(sequence), sequence, len_seq)
        temp = getMatrix(sequence, len_seq)
        if (temp== False):
            sequence = []
            continue 
        mut_pop.append(sequence)
        p+=1     
    return mut_pop


