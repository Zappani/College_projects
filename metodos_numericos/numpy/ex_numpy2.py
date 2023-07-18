import numpy as np
# Site oficial: https://numpy.org/
# Guia do Usuário: https://numpy.org/doc/stable/user/index.html
# Referência da API: https://numpy.org/doc/stable/reference/index.html

# exemplificando com lista python, portanto array que é um vetor
lp = list(range(1, 10, 2)) # criando list python a partir de um range
vnp1 = np.array(lp) # criando array numpy a partir de list
print(type(lp), lp)
print(type(vnp1), vnp1)

# usando o arange do numpy, sintaxe equivalente ao range, mas aceita passo REAL
vnp2 = np.arange(1, 10, 2)
print(type(vnp1), vnp1)

vnp3 = np.arange(0, 4.1, 0.5) # passo do arange pode ser float
print (vnp3)

# linspace trabalha com inicio, fim e QTDE DE ELEMENTOS, fim faz PARTE do array
vnp4 = np.linspace(-10, 10, 50)
print(vnp4)

vnp5 = np.arange(15) # 0 e 1 são valores default
print(vnp5)
mnp1 = np.arange(15).reshape(3, 5)
mnp2 = vnp5.reshape(5, 3)
print(mnp1)
print(mnp2)

# outros formatos padrões de criar em numpy
mnp4 = np.ones((3, 4, 4), dtype=np.int16)
mnp4[1][1][2] = 8
print(type(mnp4[1][1][2]))
print(mnp4)

mnp5 = np.zeros((3, 3))
print(type(mnp5[0][0]))
print(mnp5)

mnp6 = np.empty((5, 10), dtype=np.int64)
print(mnp6)

ma = np.arange(1, 10).reshape(3, 3)
mi = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(ma)
print(mi)
print(ma+mi) # soma de matrizes
print(ma*2) # multiplicação por escalar
mm = ma @ mi # multiplicação de matrizes, pode ser mm = ma.dot(mi)
print(mm)
mt = ma.transpose()
print(mt)
print(mt.sum()) # soma
print(mt.max()) # maior valor
print(mt.min()) # menor valor
# e assim por diante, ver na documentação!!!!
# LINKS NO COMEÇO DO CÓDIGO
