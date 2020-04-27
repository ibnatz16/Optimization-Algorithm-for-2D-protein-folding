from Debug import *
import random
from Matrix import *

def getAllContacts(folding):
    contacts = []
    for i in range(len(folding)):
        for j in range(len(folding[i])):
            if((i != j or i==j==len(folding)/2) and j < len(folding)-1 and folding[i][j].direction is not None and folding[i][j+1].direction is not None and ((folding[i][j] != folding[i][j+1].parent) and (folding[i][j].parent != folding[i][j+1]))):
                if DEBUG_1:
                    print('right', [i, j], [i,j+1], folding[i][j].direction, folding[i][j+1].direction)
                    print((folding[i][j] != folding[i][j+1].parent), (folding[i][j].parent != folding[i][j+1]))
                contacts.append([folding[i][j].index, folding[i][j+1].index])

            if((i != j or i==j==len(folding)/2) and i < len(folding) -1 and folding[i][j].direction is not None and folding[i+1][j].direction is not None and ((folding[i][j] != folding[i+1][j].parent) and (folding[i][j].parent != folding[i+1][j]))):
                if DEBUG_1:
                    print('below', [i, j],[i+1, j], folding[i][j].direction, folding[i+1][j].direction)
                    print((folding[i][j].parent != folding[i+1][j]), (folding[i][j] != folding[i+1][j].parent) )
                contacts.append([folding[i][j].index,folding[i+1][j].index])
    return contacts

def findFitnessScore(contacts, seq):

    #for testing
    sample= "MMNADMDAVAFSEMN"
    proteins =	{"A" : "H",    "C" : "H",    "I" : "H",
    "L" : "H",    "M" : "H",    "F" : "H",    "P" : "H",
    "W" : "H",    "Y" : "H",    "V" : "H",
    "R" : "P",    "N" : "P",    "D" : "P",    "Q" : "P",
    "E" : "P",    "G" : "P",
    "H" : "P",    "K" : "P",    "S" : "P",    "T" : "P" }

    # print("DSJOFIOSDSD")
    # Ans= HHPHPHPHHHHPPHP
    i=0
    ans=""
    score=0
    # print("dsafjsaokdfig")
    # print(contacts[0][0])
    # print(proteins[seq[contacts[0][0]]])
    # print(proteins[seq[contacts[0][1]]])
    while i< len(contacts):
        if(proteins[seq[contacts[i][0]]]==proteins[seq[contacts[i][1]]]=="H"):
            # print("MATCH")
            score+=1
        # else:
            # print("No match")
        i+=1
    if DEBUG_1 == 1:
        print("scores")
        print(score)
    return score

def getRandom(upper):
    x = random.randint(0, upper)
    y = random.randint(0, upper)
    if x == y:
        return getRandom(upper)
    return x, y

