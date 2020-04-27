DEBUG = False
DEBUG_1 = False
DEBUG_2 = False
DEBUG_3 = False
DEBUG_4 = False

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
