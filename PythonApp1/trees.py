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

def createLabels():
    Labels = ['A', 'B']
    return Labels

def splitDataSet(DataSet, axis, value):
    retDataSet = []

    for VerData in DataSet:
        if VerData[axis] == value:
            reduceFeat = VerData[ : axis]
            reduceFeat.extend(VerData[axis + 1 : ])
            retDataSet.append(reduceFeat)
    return retDataSet;

def chooseBestFeature(DataSet):
    num = len(DataSet[0]) - 1
    baseEntropy = calShannonEnt(DataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    for i in range(num):
        featList = [example[i] for example in DataSet]
        uniqueVal = set(featList)
        newEntropy = 0.0

        for value in uniqueVal:
            subDataSet = splitDataSet(DataSet, i,value)
            p = float(len(subDataSet)) / float(len(DataSet))
            newEntropy += p * calShannonEnt(subDataSet)

        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

def createTree(DataSet, Labels):
    classList = [example[-1] for example in DataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    if len(DataSet[0]) == 1:
        return classList[0]

    bestFeat = chooseBestFeature(DataSet)
    bestFeatLabel = Labels[bestFeat]
    myTree = {bestFeatLabel : {}}
    del(Labels[bestFeat])

    featVal = [example[bestFeat] for example in DataSet]
    uniqueVal = set(featVal)

    for value in uniqueVal:
        subLabels = Labels[ : ]
        myTree[bestFeatLabel][value] =\
            createTree(splitDataSet(DataSet, bestFeat, value), subLabels)
    
    return myTree

DataSet = createDataSet()
Labels = createLabels()
print(DataSet)
print(Labels)

#ShannonEnt = calShannonEnt(DataSet)
#print(ShannonEnt 

#retDataSet = splitDataSet(DataSet, 0, 1);
#print(retDataSet)

#bestFeature = chooseBestFeature(DataSet)
#print(bestFeature)

myTree = createTree(DataSet, Labels)
print(myTree)