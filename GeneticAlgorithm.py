from Matrix import *
from Debug import *
from Mutation import *
import sys
import random
import math

class Simulation():
    def __init__(self, file, initial, iterations, cutoff):
        self.file = file
        self.initial = initial
        self.iterations = iterations
        self.fitnessCutoff = cutoff
        self.generationScore = []
        # current generation
        self.curr = None
        # possible next generation
        self.children = None
    def initialize(self):
        generation = Generation()
        generation.seq = getData(self.file)
        if self.fitnessCutoff > len(generation.seq):
            self.fitnessCutoff = math.floor(len(generation.seq)/2)
        m = 0
        for i in range(self.initial):
            while(True):
                res = getParentGen(len(generation.seq))
                # if DEBUG_1:
                #     print(res, dirs)
                #     print(len(dirs), len(seq))
                if res != None:
                    break
            generation.dirs.append(res[0])
            generation.matrix.append(res[1])
            generation.contactPoints.append(getAllContacts(res[1]))
            if DEBUG_1:
                print(generation.dirs)
                print(generation.contactPoints)
                print(i)
            #if len(generation.contactPoints[i])is not 0:
            m+=1
            generation.score.append(findFitnessScore(generation.contactPoints[i], generation.seq))
        print('m is ', m)
        if DEBUG_1:
            print(generation.contactPoints)
        # add generation
        self.generationScore.extend(generation.score)
        print("Paret", self.generationScore)
        self.curr = generation
    ### CHECK LEGALITY, GET MATRIX FROM DIRS
    def crossOver(self):
        if DEBUG_3:
            print('crossover')
        i = 0
        self.children = Generation()

        while(i < self.initial):
            # x/y gives indices of parents
            x,y = getRandom(self.initial-1)
            if DEBUG_3:
                print(x,y)
            if DEBUG_1:
                print(len(self.curr.dirs[x])/2, len(self.curr.dirs[y])/2)
            p = self.curr
            # p1_dirs and p2_dirs are the sequence of L/F/R's for the beginning/end of generation at index x/y
            p1_dirs, p2_dirs = p.dirs[x][:self.fitnessCutoff], p.dirs[y][self.fitnessCutoff:]
            # get child
            c_dirs = p1_dirs.copy()
            c_dirs.extend(p2_dirs)
            if DEBUG_3:
                print('c_dir', c_dirs)
            c = getMatrix(c_dirs, len(self.curr.dirs[x]))
            if(c == False):
                if DEBUG_2:
                    print('returned false', x, y)
                continue
            else:
                if DEBUG_2:
                    print('true',x,y)
            # get contact points c
            c_cp = getAllContacts(c)

            # get score c
            c_sc = findFitnessScore(c_cp, self.curr.seq)
            # check that childs score is less than both of the parents
            # print('x is ', x)
            # print(' y is ', y)
            # print('child score is ', c_sc)
            # print('score matrix is \n ', p.score)
            if c_sc < p.score[x] or c_sc < p.score[y]:
                continue
            # add to pool from which we will select
            self.children.contactPoints.append(c_cp)
            self.children.dirs.append(c_dirs)
            self.children.score.append(c_sc)
            self.generationScore.append(c_sc)
            self.children.seq = self.curr.seq
            i += 1
        self.curr.dirs.extend(self.children.dirs) 
        print("crossover curr. dirs")
        print( self.curr.dirs)
class Generation():
    def __init__(self):
        self.contactPoints = []
        self.dirs = []
        self.matrix = []
        self.score = []
        self.seq = ""

def selection(sim, percent):
    # percent = int(percent)
    t = sim.generationScore
    s = sorted(sim.generationScore, reverse = True)
    # print('sorted', s)
    percent = percent/100
    # print(percent)
    top = math.floor(percent*len(s))
    # print(top)
    topFit = s[:top]
    s = s[top:]
    # print(s)
    # print(topFit)
    res = []
    res.extend(topFit)
    seq = []
    m = 0
    while(len(res)<sim.initial):
        x = random.randint(0, len(s)-1)
        res.append(s[x])
        # print('S[x]', s[x])
        # print(s)
        s.pop(x)
    # print('Res',res)
    print('T', t)
    # print('Dirs', sim.curr.dirs)
    index = []
    for j in range(len(res)):
        for i in range(len(t)):
        
            print('I is ', i)
            print('J is ', j)
            print('T[i]', t[i])
            print('Res[j]', res[j])
            if(res[j] == t[i]):
                if(i in index):
                    continue
                print('Sim', t[i])

                #####################
                # Issue here when mutations delete directions
                ###################
                print(sim.curr.dirs[i])

                seq.append(sim.curr.dirs[i])
                index.append(i)
                print(sim.curr.dirs[i])
                m+=1
                print('M',m)
                i = 0
                break
    print()
    print("selection sequence result")
    print(seq)
    return seq


#########################
# Main calls start here #
#########################

#args (file name, pop size, iterations, cutoff location for crossover, percent of selection, mutation rate(as decimal))


sim = Simulation(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
sim.initialize()
c=0
while(c<sim.iterations):
    print("before cross \n")
    print(sim.curr.dirs)
    sim.crossOver()
    # print('F', sim.generationScore)
    if DEBUG_3:
        # print children
        # print(sim.children.contactPoints)
        # print(sim.children.dirs)
        print(sorted(sim.children.score))

    sel_pop= selection(sim, float(sys.argv[5])) # returns array directions of new population 
    mut_pop= mutate(sel_pop,float(sys.argv[6])) # returns mutated population
    print("\n mutation pop")
    print(mut_pop)
    sim.curr.dirs=mut_pop
    c+=1


