from math import *
from numpy import *
from numpy.ma import ones
from numpy.core import shape

def loadDataSet():
    dataMat = []
    labelMat = []
    fp = open('testSet.txt')
    for line in fp.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmod(inX):
    return 1.0 / (1 + exp(-inX))

def graAscent01(dataMatIn, labelMatIn):
    dataMatrix = mat(dataMatIn)
    labelMatrix = mat(labelMatIn).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.0001
    maxCycle = 500
    weights = ones((n, 1))
    for k in range(maxCycle):
        h = sigmod(dataMatrix * weights)
        err = labelMatrix - h
        weights = weights + alpha * dataMatrix.transpose() * err
    return weights

def graAscent02(dataMatIn, labelMatIn):
    dataMatrix = array(dataMatIn)
    m, n = shape(dataMatIn)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmod(sum(dataMatrix[i] * weights))
        err = labelMatIn[i] - h
        offset = alpha * err * dataMatrix[i]
        weights = weights + offset
    return weights

def graAscent03(dataMatIn, labelMatIn):
    dataMatrix = array(dataMatIn) 
    m, n = shape(dataMatIn)
    weights = ones(n)
    numIter = 15
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4.0 / (i + j + 1.0) + 0.001
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmod(sum(dataMatrix[randIndex] * weights))
            err = labelMatIn[randIndex] - h
            weights = weights + alpha * err * dataMatrix[randIndex]
    return weights

dataMat, labelMat = loadDataSet()
weights = graAscent03(dataMat, labelMat)
print(weights)
