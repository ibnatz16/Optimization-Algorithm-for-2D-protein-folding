from Matrix import *
from Debug import *
from Mutation import *
from matplotlib import pyplot as plt
import sys
import random
import math
import numpy as np

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
        self.seq = 0
        self.totalScore = []
        self.totalDirs = []
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
        if DEBUG_1:
            print(generation.contactPoints)
        # add generation
        self.generationScore.extend(generation.score)
        self.curr = generation
        self.totalDirs.append([generation.score, generation.dirs])
        self.seq = len(generation.seq)
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
            c = getMatrix(c_dirs, len(self.curr.seq))
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

    def update(self,newdirs):
        #update scores and curr
        self.totalDirs.append([self.generationScore, self.curr.dirs])
        self.curr.dirs = newdirs
        self.curr.contactPoints = []
        self.curr.score = []
        average = sum(self.generationScore)/len(self.generationScore)
        self.totalScore.append([average, max(self.generationScore)])
        print('scores:', self.totalScore)
        self.generationScore = []
        for i in range(len(newdirs)):
            updatedMatrix = getMatrix(newdirs[i], len(self.curr.seq))
            if (updatedMatrix == False):
                print('update is false')
                sys.exit()
            updated_cp = getAllContacts(updatedMatrix)
            update_sc = findFitnessScore(updated_cp, self.curr.seq)
            self.curr.contactPoints.append(updated_cp)
            self.curr.score.append(update_sc)
            self.generationScore.append(update_sc)
    def selection(self, percent):
        # percent = int(percent)
        t = self.generationScore
        s = sorted(self.generationScore, reverse = True)
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
        while(len(res)<self.initial):
            x = random.randint(0, len(s)-1)
            res.append(s[x])
            # print('S[x]', s[x])
            # print(s)
            s.pop(x)
        # print('Res',res)
        if DEBUG_3:
            print('T', t)
        # print('Dirs', sim.curr.dirs)
        index = []
        i = 0
        j = 0
        while j < len(res):
            while i < len(t):
                if DEBUG_3:
                    print('I is ', i)
                    print('J is ', j)
                    print('T[i]', t[i])
                    print('T size', len(t), 'Res size', len(res))
                    print('Res[j]', res[j])
                if(res[j] == t[i]):
                    if(i in index):
                        if DEBUG_3:
                            print('Continue')
                        i+=1
                        continue
                    if DEBUG_3:
                        print('Sim', t[i])
                        print(self.curr.dirs[i])

                    seq.append(self.curr.dirs[i])
                    index.append(i)
                    m+=1
                    if DEBUG_3:
                        print(self.curr.dirs[i])
                        print('M',m)
                    i = 0
                    break
                i+=1
            j+=1
        if DEBUG_3:
            print()
            print("selection sequence result")
            print(seq)
            print('Res max', max(res), 'T max', max(t))
        return seq            

class Generation():
    def __init__(self):
        self.contactPoints = []
        self.dirs = []
        self.matrix = []
        self.score = []
        self.seq = ""

def getMin(arr):
    min = 99999
    ind = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            ind = i
    return ind, min


def getNums(upper):
    c = 0
    ret = []
    while c < 10:
        num = random.randint(0,upper-1)
        if num not in ret:
            ret.append(num)
            c+=1
    return ret

#########################
# Main calls start here #
#########################

#args (file name, pop size, iterations, cutoff location for crossover, percent of selection, mutation rate(as decimal))


sim = Simulation(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
sim.initialize()
c=0
while(c<sim.iterations):
    print("iteration", c+1)
    # print(sim.curr.dirs)
    sim.crossOver()
    if DEBUG_3:
        print(sorted(sim.children.score))
    sel_pop = sim.selection(float(sys.argv[5])) # returns array directions of new population 
    mut_pop= mutate(sel_pop,float(sys.argv[6]), sim.seq) # returns mutated population
    sim.update(mut_pop)
    c+=1


#########################
# Plots                 #
#########################
avgs = []
iterations = np.linspace(0, int(sys.argv[3]), len(sim.totalScore))
for i in range(len(sim.totalScore)):
    avgs.append(sim.totalScore[i][0])
# plt.plot(iterations, avgs)
# plt.show()
plt.savefig('FitnessVTime.png')




# randomly plot 10 foldings for first and last generation
name = 'folding_initial_'
nums = getNums(int(sys.argv[2]))
# get worst case for first generation
ind, score = getMin(sim.totalDirs[0][0])
ax = 0
proteins =	{"A" : "H",    "C" : "H",    "I" : "H",
    "L" : "H",    "M" : "H",    "F" : "H",    "P" : "H",
    "W" : "H",    "Y" : "H",    "V" : "H",
    "R" : "P",    "N" : "P",    "D" : "P",    "Q" : "P",
    "E" : "P",    "G" : "P",
    "H" : "P",    "K" : "P",    "S" : "P",    "T" : "P" }
# get x and y from matrix
print('first:')
for num in nums:
    x = []
    y = []
    c = []
    m = getSequence(sim.totalDirs[0][1][num], sim.seq)
    for i in m:
        x.append(i[0])
        y.append(i[1])
    # fill out colors
    for i in range(len(x)):
        if(proteins[sim.curr.seq[i]] == "H"):
            # print("Hydrophobic")
            c.append("red")
        else:
            # print("Hydrophillic")
            c.append("green")
    # print(x, len(x))
    # print(y, len(y))
    # print(c, len(c))
    plt.axis('off')
    plt.scatter(x,y,c=c,s=100)
    plt.plot(x,y,linestyle='dashed',color='black')
    print('score', sim.totalDirs[0][0][num])
    plt.savefig(name+str(ax)+'.png')
    plt.show()
    ax += 1
# get last generation
name = 'folding_final_'
ax = 0
print('final:')
for num in nums:
    x = []
    y = []
    c = []
    m = getSequence(sim.curr.dirs[num], sim.seq)
    for i in m:
        x.append(i[0])
        y.append(i[1])
    # fill out colors
    for i in range(len(x)):
        if(proteins[sim.curr.seq[i]] == "H"):
            # print("Hydrophobic")
            c.append("red")
        else:
            # print("Hydrophillic")
            c.append("green")
    # print(x, len(x))
    # print(y, len(y))
    # print(c, len(c))
    plt.axis('off')
    plt.scatter(x,y,c=c,s=100)
    plt.plot(x,y,linestyle='dashed',color='black')
    print('score', sim.curr.score[num])
    plt.savefig(name+str(ax)+'.png')
    plt.show()
    ax += 1
