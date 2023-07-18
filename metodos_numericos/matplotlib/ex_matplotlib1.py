import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4], [2, 3, 4, 5]);
plt.show()

eixoX = np.array([-3, -2, -1, 0, 1, 2, 3])
eixoY = pow(eixoX, 2)
plt.plot(eixoX, eixoY);
plt.show()
