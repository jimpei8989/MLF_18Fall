import numpy as np
from sklearn.linear_model import LinearRegression

T = 1000
N = 1000

def sign(x):
    return 1 if x >= 0 else -1

def f(x):
    return sign(x[0] ** 2 + x[1] ** 2 - 0.6)

def genX():
    return tuple(np.random.uniform(low = -1, high = 1, size = 2))

def genY(x):
    return f(x) if np.random.randint(low = 0, high = 10) != 0 else -f(x)

def CalcuY(X, w):
    return np.array([sign(np.dot(x, w)) for x in X])

def ErrZeroOne(Y, YY):
    return sum((0 if Y[i] == YY[i] else 1) for i in range(len(Y))) / len(Y)

EinList = list()

for t in range(T):
    raw_X = list(genX() for i in range(N))
    raw_Y = list(genY(x) for x in raw_X)
    
    trainX = np.array([np.array([1, x[0], x[1], x[0] * x[1], x[0] ** 2, x[1] ** 2]) for x in raw_X])
    trainY = np.array([y for y in raw_Y])

    reg = LinearRegression().fit(trainX, trainY)
    w_lin = reg.coef_

    #  # Print w_lin in a random way
    #  if np.random.randint(low = 0, high = 100) == 0:
    #      print(t, w_lin)

    outputY = CalcuY(trainX, w_lin)
    EinList.append(ErrZeroOne(trainY, outputY))

print("The average Ein with T =", T, "N =", N, "is", sum(EinList) / len(EinList))


