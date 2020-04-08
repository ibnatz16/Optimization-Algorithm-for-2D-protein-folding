import sys
import random
import numpy
import math

class node:
    def __init__(self, parent, child, check, direction):
        self.parent = parent
        self.child = child
        self.check = check
        self.direction = direction

def ParentGen(seqLength):
    folding = [[node(None, None, False, None) for j in range(2*seqLength)] for i in range(2*seqLength)]
    num =  math.floor(random.randint(0,3))
    direction = [["F", 1, 0 ],["L", 0, -1],["R", 0, 1]]
    previous = node(None, None, True, direction[num])
    folding[seqLength][seqLength] = previous

    if(num == 1):
        Left(direction)
    else if (num == 2):
        Right(direction)

    i = 0
    while(i < seqLength):
        num =  math.floor(random.randint(0,3))
        current = node(None, None, True, direction[num])
        i+=1


def Left(direction):
    direction = [["F", 0, -1 ],["L", -1, 0],["R", 1, 0]]

def Right(direction):
    direction = [["F", 0, 1 ],["L", 1, 0],["R", -1, 0]]

