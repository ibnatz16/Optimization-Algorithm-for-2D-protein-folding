from Matrix import *
from Debug import *
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
            if len(generation.contactPoints[i])is not 0:
                generation.score.append(findFitnessScore(generation.contactPoints[i], generation.seq))
        if DEBUG_1:
            print(generation.contactPoints)
        # add generation
        self.generationScore.append(generation.score)
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
            p1_dirs, p2_dirs = p.dirs[x][:math.floor(len(self.curr.dirs[x])/2)], p.dirs[y][math.ceil(len(self.curr.dirs[y])/2):]
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
            if c_sc < p.score[x] or c_sc < p.score[y]:
                continue
            # add to pool from which we will select
            self.children.contactPoints.append(c_cp)
            self.children.dirs.append(c)
            self.children.score.append(c_sc)
            self.children.seq = self.curr.seq
            i += 1

class Generation():
    def __init__(self):
        self.contactPoints = []
        self.dirs = []
        self.matrix = []
        self.score = []
        self.seq = ""


sim = Simulation(sys.argv[1], 10, 10, 10)
sim.initialize()
sim.crossOver()
if DEBUG_3:
    # print children
    print(sim.children.contactPoints)
    # print(sim.children.dirs)
    print(sorted(sim.children.score))
