import matplotlib.pyplot as plt
import numpy as np


eixoX = np.linspace(-3, 3, 50)
f1 = np.exp(eixoX)
f2 = np.log(eixoX)
f3 = eixoX
plt.plot(eixoX, f1)
plt.plot(eixoX, f2)
plt.plot(eixoX, f3)
plt.axis('scaled')
plt.ylim(-3, 3)
plt.show()