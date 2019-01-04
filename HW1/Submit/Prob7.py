import numpy as np
import random as rd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def InputData():
    x = []
    y = []
    for i in range(400):
        inputList = input().split()
        x.append(np.array([float(1)] + [float(x_i) for x_i in inputList[:4]]))
        y.append(int(inputList[4]))
    return x, y

def Shuffle(x, y, _seed):
    tmp = list(zip(x, y))
    rd.seed(_seed)
    rd.shuffle(tmp)
    return zip(*tmp)

def PLA(X, Y, n):
    w = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    idx = 0
    numMistakes = 0
    while True:
        for i in range(idx, idx + n):
            wx = np.dot(w, X[i])
            if Y[i] * wx <= 0:
                w = w + Y[i] * X[i]
                idx = i
                numMistakes += 1
                continue
        break
    return numMistakes

def main():
    x, y = InputData()
    ans = []
    for t in range(1126):
        _seed = t ** 29
        xp, yp = Shuffle(x, y, _seed)
        ans.append(PLA(xp, yp, 400))

    ans = sorted(ans)
    print("Average number of update is", sum(ans) / len(ans))

    # Plot
    plt.hist(ans, bins=(ans[-1] - ans[0] + 1), facecolor='green', alpha=0.75)
    plt.xlabel('Number Of Updates')
    plt.ylabel('Frequency')
    
    plt.show()


if __name__ == "__main__":
    main()
