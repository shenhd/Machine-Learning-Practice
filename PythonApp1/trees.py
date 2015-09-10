from math import log

def calShannonEnt(DataSet):
    num = len(DataSet)
    LabelCount = {}

    for FeatVec in DataSet:
        Label = FeatVec[-1]

        if Label not in LabelCount.keys():
            LabelCount[Label] = 0

        LabelCount[Label] += 1

    ShannonEnt = 0.0
    for key in LabelCount:
        p = float(LabelCount[key]) / num
        ShannonEnt -= p * log(p, 2)

    return ShannonEnt

def createDataSet():
    DataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    return DataSet

def splitDataSet(DataSet, axis, value):
    retDataSet = []

    for VerData in DataSet:
        if(VerData[axis] == value):
            retDataSet.append(VerData)
    return retDataSet;

DataSet = createDataSet()
print(DataSet)

#ShannonEnt = calShannonEnt(DataSet)
#print(ShannonEnt)

retDataSet = splitDataSet(DataSet, 0, 1);
print(retDataSet)