import sys
import random
import numpy
import math

DEBUG = False
DEBUG_1 = True
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

def printParentMatrix(folding):
    for i in range(len(folding)):
        if i == 0:
            for l in range(len(folding[i])):
                print(l, end='\t')
            print()
        for j in range(len(folding[i])):
            if folding[i][j].parent is not None:
                print(folding[i][j].parent.direction, end="\t")
            else:
                print(None, end="\t")
        print(i, end='\n')    

def getAllContacts(folding):
    contacts = []
    for i in range(len(folding)):
        for j in range(len(folding[i])):
            if(i != j and j < len(folding)-1 and folding[i][j].direction is not None and folding[i][j+1].direction is not None and ((folding[i][j] != folding[i][j+1].parent) or (folding[i][j].parent != folding[i][j+1]))):
                if DEBUG_1:
                    print('below', i, j, folding[i][j].direction, folding[i][j+1].direction)
                contacts.append([[i, j], [i, j+1]])
            elif(i != j and i < len(folding) -1 and folding[i][j].direction is not None and folding[i+1][j].direction is not None and ((folding[i][j] != folding[i+1][j].parent) or (folding[i][j].parent != folding[i+1][j]))):
                if DEBUG_1:
                    print('above', i, j, folding[i][j].direction, folding[i+1][j].direction)
                contacts.append([[i, j],[i+1,j]])
    return contacts

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
            return None
            # return ParentGen(seqLength)
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

while(True):
    res = ParentGen(int(sys.argv[1]))
    if res != None:
        break
dirs, matrix = res
printMatrix(matrix)
printParentMatrix(matrix)
contacts = getAllContacts(matrix)
print(dirs)
for i in contacts:
    print(i)