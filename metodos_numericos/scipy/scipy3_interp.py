# Exemplo de Interpolação

# função de interpolação: interp1d
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

qtdePontos = 8
pontos = np.random.random(qtdePontos)
ruido = (pontos *2 - 1) * 0.1 # criando um ruído/variação
#print(pontos)
#print(ruido)

# simular dados de um experimento medido
x = np.linspace(0, 1, qtdePontos)
fx = np.sin(2 * np.pi * x) + ruido # pontos fx ficaram 'perto' do seno

interpolacao_linear = interp1d(x, fx)  # chamada padrão é linear
x2 = np.linspace(0, 1, 100)
fx2 = interpolacao_linear (x2)

interpolacao_cubica = interp1d(x, fx, kind="cubic") # chamada passar parâmetro opcional 
fx3 = interpolacao_cubica(x2)

plt.plot(x, fx, 'ro', label="Medição")
plt.plot(x2, fx2, label="Interp Linear")
plt.plot(x2, fx3, label="Interp Cubica")
plt.legend()
plt.show()
