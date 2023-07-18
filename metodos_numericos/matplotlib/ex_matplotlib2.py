import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
print(type(x))
plt.plot(x, [2, 3, 4, 5]);
plt.plot(x, [3, 4, 5, 6]);
plt.plot(x, [4, 5, 6, 7]);
plt.show()

eixoX = np.array([-3, -1, 0, 1,  3])
eixoY = 2 + pow(eixoX, 2)
print(eixoY)
print(type(eixoY))
plt.plot(eixoX, eixoY, color='cyan');

eixoX = np.array([-3, -2, -1, 0, 1, 2, 3])
eixoY = pow(eixoX, 2)
plt.plot(eixoX, eixoY, color='red');

eixoX = np.linspace(-3, 3, 50)
eixoY = -2 + pow(eixoX, 2)
plt.plot(eixoX, eixoY, color='black');
plt.show()


x = np.arange(-4, 5, 1)
y = np.random.randint(3, 9, 9)
print(x)
print(y)
plt.plot(x, y, ls='--', lw=2, color='b', marker='o', ms=10, mfc='hotpink')
plt.show()
# olhar estilos de linha, cor e marker no linK:
# https://www.w3schools.com/python/matplotlib_markers.asp
# ver linestyle ou ls (''ou none apenas os pontos)
# ver linewith ou lw
# ver marker
# ver markersize ou ms
# ver markerfacecolor ou mfc
# ver markeredgecolor ou mec

eixo_x = np.linspace(-10, 10, 22)
eixo_y = eixo_x ** 3
plt.plot(eixo_x, eixo_y, '--og') 
plt.show()