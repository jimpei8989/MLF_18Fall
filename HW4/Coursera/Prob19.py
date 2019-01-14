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

tpX, tpY = readData('hw4_train.dat')
testX,  testY  = readData('hw4_test.dat')

ans = list()

for t in range(2, -11, -1):
    lamb = 10 ** t
    E_CV = 0
    for i in range(5):
        trainX = np.concatenate((tpX[:i * 40, :], tpX[(i + 1) * 40:, :]), axis = 0)
        trainY = np.concatenate((tpY[:i * 40, :], tpY[(i + 1) * 40:, :]), axis = 0)

        evalX = tpX[i * 40 : (i + 1) * 40]
        evalY = tpY[i * 40 : (i + 1) * 40]

        W_REG = np.dot(np.dot(np.linalg.inv(np.dot(trainX.T, trainX) + lamb * np.identity(trainX.shape[1])), trainX.T), trainY)
        E_CV += (ErrZeroOne(W_REG, evalX, evalY)) / 5
    ans.append((t, E_CV))

for line in ans:
    print('\t'.join(str(e) for e in line))

