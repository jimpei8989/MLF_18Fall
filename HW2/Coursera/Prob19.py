import numpy as np


def Sign(x):
    return 1 if x >= 0.0 else -1

def F(x):
    return Sign(x) if np.random.rand() < 0.8 else -Sign(x)

def H(x, s, theta):
    return s * Sign(x - theta)

trainFile = open("hw2_train.dat", "r")
testFile = open("hw2_test.dat", "r")

trainInput = [s.split() for s in trainFile.readlines()]
trainX = [[float(x) for x in xs[:-1]] for xs in trainInput]
trainY = [float(ys[-1]) for ys in trainInput]
trainN = len(trainX)

testInput = [s.split() for s in testFile.readlines()]
testX = [[float(x) for x in xs[:-1]] for xs in testInput]
testY = [float(ys[-1]) for ys in testInput]
testN = len(testX)

D = len(trainX[0])

bestEin = 1
bestD, bestH = -1, (-1, -1)

for d in range(D):
    X = [x[d] for x in trainX]
    Y = trainY
    ein = 1
    localH = (-1, -1)

    for s in [-1, 1]:
        for theta in [x - 0.0001 for x in X]:
            err = 0
            for i in range(trainN):
                x, y = X[i], Y[i]
                if H(x, s, theta) != y:
                    err += 1
            if err / trainN < ein:
                ein = err / trainN
                localH = (s, theta)
    if ein < bestEin:
        bestD = d
        bestH = localH
        bestEin = ein

print(bestD, bestEin, bestH)

err = 0
X = [x[bestD] for x in testX]
Y = testY
S, Theta = bestH

for i in range(testN):
    x, y = X[i], Y[i]
    if H(x, S, Theta) != y:
        err += 1

print(err / testN)
