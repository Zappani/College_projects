import matplotlib.pyplot as plt
import numpy as np


eixoX = np.linspace(-3, 3, 50)
f1 = np.exp(eixoX)
f2 = np.log(eixoX)
f3 = eixoX
plt.plot(eixoX, f1, label='f(x) = eˆx') # label é o 'nome' do gráfico
plt.plot(eixoX, f2, label='g(x) = ln(x)')
plt.plot(eixoX, f3, label='h(x) = x')
plt.axis('scaled') # forçar a mesma escala para eixos X e Y
plt.ylim(-3, 3) # limites para o eixo Y
plt.legend() # mostrar a legenda, enviado como label para o plot
plt.show()




# criando 4 ploagens (2 linhas e 2 colunas)
# subplot permitem diversas áreas de plotagem
plt.subplots(nrows=2, ncols=2)
plt.show()

eX = np.arange(-3, 4, 0.2)
eY = eX ** 2 - 3
plt.subplot(1, 2, 1)
plt.plot(eX, eY, '*g-')

plt.subplot(1, 2, 2)
eY = eY * -1
plt.plot(eX, eY, 'or-')
plt.show()


def f(x):
    return x

def g(x):
    return x**2

eixo_x = np.linspace(0, 1, 20)
print(eixo_x)

plot_f = f(eixo_x)
print(plot_f)
plot_g = g(eixo_x)
plt.plot(eixo_x, plot_f)
plt.plot(eixo_x, plot_g)
plt.fill_between(eixo_x, plot_f, plot_g, color='y', alpha= 0.3, hatch='O')
plt.show()
