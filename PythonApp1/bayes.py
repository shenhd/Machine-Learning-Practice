from numpy.ma import ones, zeros, log

#posting and class for training
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec

#create vocabulary list for training
def createVocabList(DataSet):
    vocabList = set([])
    for doc in DataSet:
        vocabList = vocabList | set(doc)
    return list(vocabList)

#set the input file into vetor stand for vocaList
def setWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else :
            print("the word %s is not in my vocabulary" % word)
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWord = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = zeros(numWord)
    p1Num = zeros(numWord)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p0Vect = p0Num / p0Denom
    p1Vect = p1Num / p1Denom
    return p0Vect, p1Vect, pAbusive


def trainNB1(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWord = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWord)
    p1Num = ones(numWord)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p0Vect = log(p0Num / p0Denom)
    p1Vect = log(p1Num / p1Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(inputVec, p0Vect, p1Vect, pAbsive):
    p0 = sum(inputVec * p0Vect) + log(1 - pAbsive)
    p1 = sum(inputVec * p1Vect) + log(pAbsive)
    if p1 > p0:
        return 1
    else:
        return 0


#test code
PostingList, ClassVec = loadDataSet();
VocabList = createVocabList(PostingList)
print(VocabList)
#WordVec = setWord2Vec(VocaList, PostingList[0])
#print(WordVec)
trainMat = []
for post in PostingList:
    trainMat.append(setWord2Vec(VocabList, post))

P0Vect, P1Vect, PAbsive = trainNB1(trainMat, ClassVec)
print(P0Vect)
print(P1Vect)
print(PAbsive)

testList1 = ['love', 'my', 'dog']
testList2 = ['stupid', 'garbage']

testVec1 = setWord2Vec(VocabList, testList1)
testVec2 = setWord2Vec(VocabList, testList2)

res1 = classifyNB(testVec1, P0Vect, P1Vect, PAbsive)
res2 = classifyNB(testVec2, P0Vect, P1Vect, PAbsive)

print(res1)
print(res2)