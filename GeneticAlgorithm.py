from ParentGen import *
from Debug import *
import sys
seq = getData(sys.argv[1])
print(seq)
# sys.exit()
seq = "MMNADMDAVDAENQVELEEKTRLINQVMELQHTLEDLSARVDAVKEENLKLKSENQVLGQYIENLMSASSVFQTTDTKSKRK"
while(True):
    res = ParentGen(len(seq))
    # if DEBUG_1:
    #     print(res, dirs)
    #     print(len(dirs), len(seq))
    if res != None:
        break
dirs, matrix = res
contacts = getAllContacts(matrix)

if DEBUG_1:
    print(dirs)
    for i in contacts:
        print(i)
    printMatrix(matrix)
    printParentMatrix(matrix)
    print(dirs)
    for i in contacts:
        print(i)

if len(contacts)is not 0:
    findFitnessScore(contacts, seq)
