# Site oficial: https://numpy.org/
# Guia do Usuário: https://numpy.org/doc/stable/user/index.html
# Referência da API: https://numpy.org/doc/stable/reference/index.html

import numpy as np
# ARRAYS UNIDIMENSIONAIS - VETORES
# exemplificando com lista python, portanto array que é um vetor
'''
l = [1, 2, 3, 4.2] # lista Python
print(l) # l é um vetor Python
print(l[-1]) # ultimo posicao de l
print(type(l))
print(type(l[0]))
print(type(l[3]))

vnp = np.array(l) # criando array numpy a partir de lista
print(vnp)
print(vnp[1]) # segundo índice de vnp
print(type(vnp)) # <class 'numpy.ndarray'>
print(vnp.dtype) # tipo via numpy: float64 (64 bits)
print(type(vnp[0]))# tipo via python: <class 'numpy.float64'>
print(vnp.dtype.name) # nome do tipo via numpy
print(vnp.itemsize) # 8, total de byte de um item do array
print(vnp.size) # 4, total de itens no array
print(vnp.ndim) # 1, total de dimensoes, no caso do vetor, uma dimensão
print(vnp.shape) # retorna tupla com as dimensões do array: (4,)
print()
'''

# ARRAYS MULTIDIMENSIONAIS - MATRIZES
# exemplificando com lista de lista python, portanto array que é uma matriz
ll = [[1, 2, 3],
      [4, 5, 6]]
print(ll) # ll é matriz python
print(ll[0][0])
print(type(ll))

mnp = np.array(ll) # criando array numpy a partir de lista
print(mnp)
print(mnp[1][1])
print(type(mnp)) # tipo da estrutura: <class 'numpy.ndarray'>
print(mnp.dtype) # tipo via numpy: int64 (64 bits)
print(type(mnp[0]))# tipo via python da linha: <class 'numpy.ndarray'>
print(type(mnp[0][0]))# tipo via python da posição: <class 'numpy.int64'>
print(mnp.dtype.name) # nome do tipo via numpy
print(mnp.itemsize) # 8, total de bytes de um item do array, ou seja, de um int64
print(mnp.size) # 6, total de itens no array = qtde de posições
print(mnp.ndim) # 2, total de dimensões, no caso de matiz, duas dimensões
print(mnp.shape) # retorna tupla com as dimensões do array: (2, 3)
