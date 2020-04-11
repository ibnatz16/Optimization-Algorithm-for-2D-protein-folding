from ParentGen import *
from Debug import *
import sys
import random

class Simulation():
    def __init__(self, file, initial, iterations, cutoff, generationScore):
        self.file = file
        self.initial = initial
        self.iterations = iterations
        self.fitnessCutoff = cutoff
        self.generationScore = generationScore
        self.curr = None
    def initialize(self):
        seq = getData(self.file)
        generation = Generation()
        for i in range(self.initial):
            while(True):
                res = getParentGen(len(seq))
                # if DEBUG_1:
                #     print(res, dirs)
                #     print(len(dirs), len(seq))
                if res != None:
                    break
            generation.dirs.append(res[0])
            generation.matrix.append(res[1])
            generation.contactPoints.append(getAllContacts(res[1]))
            print(generation.dirs)
            print(generation.contactPoints)
            print(i)
            if len(generation.contactPoints[i])is not 0:
                generation.score = findFitnessScore(generation.contactPoints[i], seq)
        print(generation.contactPoints)
        # add generation
        self.generationScore.append(generation.score)
        self.curr = generation
        self.index += 1
    def crossOver(self):
            x,y = getRandom(len(self.initial)-1)
            
class Generation():
    def __init__(self):
        self.contactPoints = []
        self.dirs = []
        self.matrix = []
        self.score = -1
        self.seq = ""


sim = Simulation(sys.argv[1], 10, 10, 10, None)
sim.initialize()
