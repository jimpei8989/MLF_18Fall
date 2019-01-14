import numpy as np
import matplotlib.pyplot as plt

def readData(filename):
    data = np.loadtxt(filename)
    r, c = data.shape
    X = np.concatenate((np.ones((r, 1)), data[:, : -1]), axis = 1)
    Y = data[:, -1:]
    return X, Y

def GradientEin(w, X, Y):
    theta = Theta(-Y * np.dot(X, w))
    return -1 * (Y * X).T.dot(theta) / X.shape[0]

def ErrZeroOne(w, X, Y):
    return np.sum(np.sign(np.dot(X, w)) != Y) / X.shape[0]

trainX, trainY = readData('hw4_train.dat')
testX,  testY  = readData('hw4_test.dat')

lamb = 10

W_REG = np.dot(np.dot(np.linalg.inv(np.dot(trainX.T, trainX) + lamb * np.identity(trainX.shape[1])), trainX.T), trainY)

print("W_REG =", W_REG)
print("E_in   =", ErrZeroOne(W_REG, trainX, trainY))
print("E_out  =", ErrZeroOne(W_REG, testX, testY))
