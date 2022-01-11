import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2)

y = np.random.normal(0,1,1000)
y1 = np.random.rand(1000)

axes[0].hist(y)
axes[1].hist(y1)

axes[0].title.set_text('normal')
axes[1].title.set_text('random')

axes[0].set_xlabel('value')
axes[1].set_xlabel('value')

axes[0].set_ylabel('frequency')

plt.show()