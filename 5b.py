import numpy as np
import matplotlib.pyplot as plt
y = np.random.normal(0,1,1000)
plt.hist(y, label='random',range=[-2,2])
plt.show()