import numpy as np
import matplotlib.pyplot as plt

def Sign(x):
    return 1 if x >= 0.0 else -1

def F(x):
    return Sign(x) if np.random.rand() < 0.8 else -Sign(x)

def H(x, s, theta):
    return s * Sign(x - theta)

dE = list()

for test in range(1000):
    X = np.random.uniform(-1, 1, 20)
    Y = [F(x) for x in X]
    
    ein, eout = 100000000, 0
    
    for s in [-1, 1]:
        for theta in [x - 0.00001 for x in X]:
            err = 0
            for i in range(len(X)):
                x, y = X[i], Y[i]
                if H(x, s, theta) != y:
                    err += 1
            if err / len(X) < ein:
                ein = err / len(X)
                eout = 0.5 + 0.3 * s * (abs(theta) - 1)
    dE.append(ein - eout)

# Print the result
print("The average Ein-Eout is", np.mean(dE))

# Plot
plt.hist(dE, bins = 30, facecolor='green', alpha=0.75)
plt.xlabel('Ein - Eout')
plt.ylabel('Frequency')
plt.show()

