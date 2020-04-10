import sys
import random
import numpy
import math
from Score import *

def getData(argIn):
    f = open(argIn, "r")
    # o = open(output, "w")
    line = f.readline()
    seqn = 0
    seq = ""
    while line:
        if(not line.startswith('>')):
            # sequence to print
            seqn = seqn+1
            frag = 0
            # iterate through sequence and chop it into blocks
            i = 0
            seqlen= len(line)
            seq=line
            # print(seqlen)
            # print(seq)
        line = f.readline().strip()
    # o.close()
    f.close()
    return seq

class node:
    def __init__(self, parent, child, check, direction, counter):
        self.parent = parent
        self.child = child
        self.check = check
        self.index = counter
        if direction is not None:
            self.direction = direction.copy()
        else:
            self.direction = None

def ParentGen(seqLength):
    folding = [[node(None, None, False, None, -1) for j in range(2*seqLength)] for i in range(2*seqLength)]
    dirs = []
    # index in dirs array
    count = 0
    num =  random.randrange(3)

    if DEBUG:
        print("Initial Folding Matrix")
        printMatrix(folding)
        print('Initial random val:', num)
    direction = [["F", 0, 1 ],["L", -1, 0],["R", 1, 0]]
    row = seqLength
    col = seqLength
    dirs.append(direction[num][0])
    prev = node(None, None, True, direction[num], count)
    count += 1
    folding[row][col] = prev
    if DEBUG:
        print('Initial direction:', direction, direction[num])
        print('Update Matrix')
        printMatrix(folding)
        print(dirs)
        print('num', num)
        print('direction', direction[num])
        print(col, row)
    row += direction[num][2]
    col += direction[num][1]
    if(num == 1):
        direction = Left(direction)
    elif (num == 2):
        direction = Right(direction)
    if DEBUG:
        print('after direction', direction)
        print(col, row)
    i = 0
    possible = 0
    while(i < seqLength-1):
        # get direction
        num =  random.randrange(3)
        curr = node(prev, None, True, direction[num], count)
        count += 1

        # make sure position is open
        if folding[row+direction[num][2]][col+direction[num][1]].check == True:
            if DEBUG:
                print('repeat')
                print('\n\n\n\n\n\n\n\n\n\n---------------------------------- REPEAT ----------------------------\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n')
            if DEBUG_1:
                print(count, seqLength, dirs, folding[row+direction[num][2]][col+direction[num][1]], num)
            count -= 1
            possible += 1
            # restart
            if possible == 3:
                folding = [[node(None, None, False, None, -1) for j in range(2*seqLength)] for i in range(2*seqLength)]
                dirs = []
                row = seqLength
                col = seqLength
                possible = 0
                # index in dirs array
                count = 0
                i = 0
                continue
            continue
            return None, dirs
        possible = 0
        folding[row][col] = curr
        # add to directions list
        dirs.append(direction[num][0])

        if DEBUG:
            print('Update Matrix')
            printMatrix(folding)
            print(dirs)
            print('num', num)
            print('direction', direction[num])
            print(col, row)

        # move
        row += direction[num][2]
        col += direction[num][1]
        # curr is new parent
        prev = curr
        # update direction
        if(num == 1):
            direction = Left(direction)
        elif (num == 2):
            direction = Right(direction)
        else:
            if DEBUG:
                print('Forward', direction)
        if DEBUG:
            print('after direction', direction)
            print(col, row)
        i+=1
    return dirs, folding

def getdirL(arr):
    if arr[2] == 0:
        return [arr[0], arr[2], arr[1]]
    return [arr[0], -arr[2], -arr[1]]
def getdirR(arr):
    if arr[1] == 0:
        return [arr[0], arr[2], arr[1]]
    return [arr[0], -arr[2], -arr[1]]

def Left(direction):
    f = getdirL(direction[0])
    l = getdirL(direction[1])
    r = getdirL(direction[2])
    if DEBUG:
        print('Left', f, l, r)
    return [f, l, r]

def Right(direction):
    f = getdirR(direction[0])
    l = getdirR(direction[1])
    r = getdirR(direction[2])
    if DEBUG:
        print('Right', f, l, r)
    return [f, l, r]
