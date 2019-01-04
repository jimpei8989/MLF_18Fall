import numpy as np
import matplotlib.pyplot as plt

# Ploting
Ein_FGD = list(np.random.uniform(low = 0, high = 1, size = 100))
Ein_SGD = list(np.random.uniform(low = 0, high = 1, size = 100))
t_axis = [i for i in range(100)]

plt.plot(Ein_FGD, t_axis, 'g', Ein_SGD, t_axis, 'b')
plt.xlabel("t")
plt.ylabel("Ein(w_t)")
plt.show()

