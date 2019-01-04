import math
import numpy as np

def readData(filename):
    X, Y = list(), list()
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            X.append(np.array([1] + [float(x) for x in data[:-1]]))
            Y.append(int(data[-1]))
    return X, Y

def sign(x):
    return 1 if x >= 0 else -1

def Theta(s):
    return 1 / (1 + np.exp(-s))

def GradientEin(w, X, Y):
    return sum(Theta(-Y[n] * np.dot(w, X[n])) * (-Y[n] * X[n]) for n in range(len(X))) / len(X)

def ErrZeroOne(w, X, Y):
    return sum(0 if sign(np.dot(w, X[i])) == Y[i] else 1 for i in range(len(X))) / len(X)

T = 2000
ita = 0.01

trainX, trainY = readData('hw3_train.dat')
testX, testY = readData('hw3_test.dat')

D = len(trainX[0])

w = np.array([0] * D)

for t in range(T):
    w = w - ita * GradientEin(w, trainX, trainY)

print("Problem 19:")
print("w =", w)
print("Ein =", ErrZeroOne(w, trainX, trainY))
print("Eout =", ErrZeroOne(w, testX, testY))
