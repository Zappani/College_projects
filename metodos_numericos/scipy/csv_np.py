import matplotlib.pyplot as plt
import numpy as np

eixoX = []
eixoY = []

eixoX, eixoY = np.loadtxt(r'C:\Users\User\OneDrive - ufpr.br\faculdade\materias\metodos numericos\aulas\05.11\teste.csv', delimiter=',', unpack=True)
print (eixoX)
print (eixoY)

# 'plano cartesiano'
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Mover eixos x e y para o meio passando por (0, 0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# remover eixos superior e direito
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.axis("scaled") 
plt.xlim(-4, 4)
plt.ylim(-4, 4)

plt.plot(eixoX ,eixoY, label='xˆ2 -4x + 3')
plt.xlabel('x', loc='right')
plt.ylabel('f(x)', loc='top')
plt.title('Dados do CSV')
plt.legend()
plt.show()
