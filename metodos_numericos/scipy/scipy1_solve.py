'''
Scipy: 
- ́algebra linear (scipy.linalg)
- integração numerica (scipy.integrate)
- interpolação (scipy.interpolate)
- otimização (scipy.optimize)
- estatística (scipy.stats)
- etc
'''

from scipy import linalg
# Guia do usuário: https://docs.scipy.org/doc/scipy/tutorial/index.html 
# Referência: https://docs.scipy.org/doc/scipy/reference/ 
import numpy as np

# 1) Exemplo para resolução de sistemas de equacoes lineares
# função de cálculo: linalg.solve
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html
#
# Equação da forma: 
#       a11x1 + a12x2+ a13x3 + ... + a1nxn = b1
#       a21x1 + a22x2+ a23x3 + ... + a2nxn = b2
#         ...       ...               ...
#       an1x1 + an2x2+ an3x3 + ... + annxn = bn
# Sendo:
#       aij: coeficientes  i,j = 1..n
#        xj: variáveis       j = 1..n
#        bi: constantes      i = 1..n
# Representado matricialmente por
#        Ax = b
# Sendo:
#        A: matriz dos coeficientes
#        x: vetor das variáveis
#        b: vetor de constantes

# A) Para o sistema:
#       3x1 +  x2 = 9
#        x1 + 2x2 = 8

a = np.array([[3, 1], [1, 2]]) # matriz dos coeficientes
b = np.array([9, 8]) # vetor de constantes
x = linalg.solve(a, b) # devolve um ndarray 1..n como vetor solução
print ("Valor de x1: ", x[0])
print ("Valor de x2: ", x[1])

# B) Para o sistema:
#       3x1 +  2x2 + 4x3 = 1
#        x1 +   x2 + 2x3 = 2
#       4x1 +  3x2 + 2x3 = 3

a = np.array([[3, 2, 4], [1, 1, 2], [4, 3, 2]]) # matriz dos coeficientes
b = np.array([1, 2, 3]) # vetor de constantes
x = linalg.solve(a, b) # devolve um ndarray 1..n como vetor solução
print ("Valor de x1: ", x[0])
print ("Valor de x2: ", x[1])
print ("Valor de x3: ", x[2])


