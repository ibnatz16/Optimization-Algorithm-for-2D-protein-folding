import sys
import random
import numpy
import math

DEBUG = False

class node:
    def __init__(self, parent, child, check, direction):
        self.parent = parent
        self.child = child
        self.check = check
        if direction is not None:
            self.direction = direction.copy()
        else:
            self.direction = None
        

def printMatrix(folding):
    for i in range(len(folding)):
        if i == 0:
            for l in range(len(folding[i])):
                print(l, end='\t')
            print()
        for j in range(len(folding[i])):
            print(folding[i][j].direction, end="\t")
        print(i, end='\n')


def getAllContacts(folding):
    contacts = []
    for i in range(len(folding)):
        for j in range(len(folding[i])):
            # upper left
            if i ==0 and j == 0:
            # top row
            elif i ==0:
            # left column
            elif j ==0:
            # right column
            elif j == len(folding[i])-1:
            # bottom row
            elif i == len(folding[i])-1:
            else:

def ParentGen(seqLength):
    folding = [[node(None, None, False, None) for j in range(2*seqLength)] for i in range(2*seqLength)]
    dirs = []
    num =  random.randrange(3)
    if DEBUG:
        print("Initial Folding Matrix")
        printMatrix(folding)
        print('Initial random val:', num)
    direction = [["F", 0, 1 ],["L", -1, 0],["R", 1, 0]]
    row = seqLength
    col = seqLength
    dirs.append(direction[num][0])
    prev = node(None, None, True, direction[num])
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
    while(i < seqLength-1):
        # get direction
        num =  random.randrange(3)
        curr = node(prev, None, True, direction[num])
        # make sure position is open
        if folding[row][col].check == True:
            if DEBUG:
                print('repeat')
                print('\n\n\n\n\n\n\n\n\n\n---------------------------------- REPEAT ----------------------------\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n')
            return ParentGen(seqLength)
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

dirs, matrix = ParentGen(int(sys.argv[1]))