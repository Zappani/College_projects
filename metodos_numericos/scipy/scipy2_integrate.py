# Exemplo de integral definida com módulo Integrate do SciPy

# função de cálculo: integrate.quad
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(0, 4, 20)
fx = f(x)

aAprox = integrate.quad(f, 0, 4)
print ("Tupla retornada: ", aAprox)

plt.plot(x, fx, label='f(x) = xˆ2')
titulo = 'Área aproximada x^2, de 0 a 4: ' + str(round(aAprox[0], 4))
titulo += '\nErro estimado: ' + str(aAprox[1])
plt.title(titulo)
plt.fill_between(x, fx, color = "blue", alpha = 0.3, hatch = '|')
plt.legend()
plt.show()
