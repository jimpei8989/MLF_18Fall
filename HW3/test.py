import math
import numpy as np
import matplotlib.pyplot as plt

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
ita_FGD = 0.01
ita_SGD = 0.001

trainX, trainY = readData('hw3_train.dat')
testX, testY = readData('hw3_test.dat')

D = len(trainX[0])

w_FGD = np.array([0] * D)
w_SGD = np.array([0] * D)

Ein_FGD = list()
Ein_SGD = list()
Eout_FGD = list()
Eout_SGD = list()

for t in range(T):
    #  # Fixed rate Gradient Descent
    #  w_FGD = w_FGD - ita_FGD * GradientEin(w_FGD, trainX, trainY)
    #  Ein_FGD.append(ErrZeroOne(w_FGD, trainX, trainY))
    #  Eout_FGD.append(ErrZeroOne(w_FGD, testX, testY))

    # Stochatist Gradient Descent
    x, y = trainX[t % len(trainX)], trainY[t % len(trainX)]
    w_SGD = w_SGD - ita_SGD * Theta(-y * np.dot(w_SGD, x)) * (-y * x)
    Ein_SGD.append(ErrZeroOne(w_SGD, trainX, trainY))
    Eout_SGD.append(ErrZeroOne(w_SGD, testX, testY))

print("Problem 4 & 5:")
#  print("Fixed rate Gradient Descent")
#  print("Ein =", Ein_FGD[-1])
#  print("Eout =", Eout_FGD[-1])

print("")
print("Stochatist Gradient Descent")
print("Ein =", Ein_SGD[-1])
print("Eout =", Eout_SGD[-1])

t_axis = [t for t in range(T)]

# Ploting
plt.figure(1)
#  plt.plot(t_axis, Ein_FGD, 'g', label = "Fixed rate")
plt.plot(t_axis, Ein_SGD, 'b', label = "Stochatist")
plt.title("Problem 4 : Ein / t")
plt.xlabel("t")
plt.ylabel("Ein(w_t)")
plt.label("upper right")
plt.show()

plt.figure(2)
#  plt.plot(t_axis, Eout_FGD, 'g', label = "Fixed rate")
plt.plot(t_axis, Eout_SGD, 'b', label = "Stochatist")
plt.title("Problem 5 : Eout / t")
plt.xlabel("t")
plt.ylabel("Eout(w_t)")
plt.show()

