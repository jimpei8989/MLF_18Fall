# Thanks to Mama and Piepie, who brought me into the world of Python

import numpy as np
import matplotlib.pyplot as plt

def readData(filename):
    data = np.loadtxt(filename)
    r, c = data.shape
    X = np.concatenate((np.ones((r, 1)), data[:, : -1]), axis = 1)
    Y = data[:, -1:]
    return X, Y

def Theta(s):
    return 1 / (1 + np.exp(-s))

def GradientEin(w, X, Y):
    theta = Theta(-Y * np.dot(X, w))
    return -1 * (Y * X).T.dot(theta) / X.shape[0]

def ErrZeroOne(w, X, Y):
    return np.sum(np.sign(np.dot(X, w)) != Y) / X.shape[0]

T = 2000 
eta_FGD = 0.01
eta_SGD = 0.001

trainX, trainY = readData('hw3_train.dat')
testX,  testY  = readData('hw3_test.dat')

D = len(trainX[0])

w_FGD = np.zeros((D, 1))
w_SGD = np.zeros((D, 1))

Ein_FGD = np.zeros(T)
Ein_SGD = np.zeros(T)
Eout_FGD = np.zeros(T)
Eout_SGD = np.zeros(T)

for t in range(T):
    # Fixed rate Gradient Descent
    w_FGD = w_FGD - eta_FGD * GradientEin(w_FGD, trainX, trainY)
    Ein_FGD[t]  = ErrZeroOne(w_FGD, trainX, trainY)
    Eout_FGD[t] = ErrZeroOne(w_FGD, testX,  testY)

    # Stochatist Gradient Descent
    x, y = np.array(trainX[t % trainX.shape[0]]).reshape(-1, 1), trainY[t % trainX.shape[0]]
    w_SGD = w_SGD - eta_SGD * Theta(-y * np.dot(x.T, w_SGD)) * (-y * x)
    Ein_SGD[t]  = ErrZeroOne(w_SGD, trainX, trainY)
    Eout_SGD[t] = ErrZeroOne(w_SGD, testX, testY)

print("Problem 4 & 5:")
print("Fixed rate Gradient Descent")
print("Ein =", Ein_FGD[-1])
print("Eout =", Eout_FGD[-1])

print("")
print("Stochatist Gradient Descent")
print("Ein =", Ein_SGD[-1])
print("Eout =", Eout_SGD[-1])

t_axis = [t for t in range(T)]

plt.figure(1)
plt.plot(t_axis, Ein_FGD, 'g', label = "Fixed rate")
plt.plot(t_axis, Ein_SGD, 'b', label = "Stochatist")
plt.title("Problem 4 - $E_{in}(\mathbf{w}_t) : t$")
plt.xlabel("$t$")
plt.ylabel("$E_{in}(\mathbf{w}_t)$")
plt.legend()
fig1 = plt.gcf()

plt.figure(2)
plt.plot(t_axis, Eout_FGD, 'g', label = "Fixed rate")
plt.plot(t_axis, Eout_SGD, 'b', label = "Stochatist")
plt.title("Problem 5 - $E_{out}(\mathbf{w}_t) : t$")
plt.xlabel("$t$")
plt.ylabel("$E_{out}(\mathbf{w}_t)$")
plt.legend()
fig2 = plt.gcf()

fig1.savefig("ExpResult/Ein_" + str(T) + ".png", dpi=400)
fig2.savefig("ExpResult/Eout_" + str(T) + ".png", dpi=400)
