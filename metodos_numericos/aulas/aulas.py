# Aula 1 - Intro
'''

nome = input("Nome? ") # nome será um str de string
i = 7 # int de integer
f = 8.5 # float, ponto flutuante (real) 
b = True # bool, boolena, lógica
print(nome, type(nome)) 
print(i, type(i))
print(f, type(f))
print(b, type(b))

i = int(input("Quantos filhos: ")) # type casting, coerção
print(f"{nome.upper()}, se nascer mais um, você terá {i+1} filhos.")
print(f"{nome} tem {len(nome)} letras") # len len comprimento
'''

# Aula 2 - Loops
'''

n = int(input("Numero? "))

# uso do loop WHILE, inicio, condicao e incremento
# escritos em momentos separado
cont = 1
while cont <= 10:
    print(f"{cont:2} * {n} = {cont*n}")
    cont += 1 # incremento, idem a cont = cont + 1

# uso do loop FOR que demanda o RANGE
for cont in range(-10, 11, 3):
    print(f"{cont:2} * {n} = {cont*n}")
'''
    
# Aula 3 - Loops e Intro a listas
'''  
    #parte 1

mercado = ["ovos", "banana", "alface", "detergente"]
# indices     0        1         2           3
#             -4        -3       -2          -1
print(len(mercado))
print(mercado[0])
print(mercado[-1])

# loop tradicional para percorrer a lista (ciente da posição)
for i in range(0, len(mercado), 1):
    print(f"Produto {i}: {mercado[i]}")

# loop for each, objetivo é pegar o conteudo (nao posicao)
print("Para comprar: ",  end="") # evitar pular a linha
for item in mercado:
    print(f"{item}", end=", ")
# bricando com alguns métodos da classe list
# que é uma lista dinâmica 
# olhar em: https://www.w3schools.com/python/python_lists_methods.asp
print()
print(mercado)
mercado.append("acelga")
mercado.append("cebola")
print(mercado)
mercado.sort()
print(mercado)
mercado.reverse()
print(mercado)

vet1 = [1, 3, 5, 7, 9]
vet2 = [0]*10
vet3 = []
print(f"Vetor: {vet1}, comprimento: {len(vet1)}")
print(f"Vetor: {vet2}, comprimento: {len(vet2)}")
print(f"Vetor: {vet3}, comprimento: {len(vet3)}")

    #parte 2

# lista inicializada
mercado = ["acelga", "banana", "alface", "detergente"]
# indices     0        1         2           3
#             -4        -3       -2          -1
print(len(mercado))
print(mercado[0])
print(mercado[-1])

# loop tradicional para percorrer a lista (ciente da posição)
for i in range(0, len(mercado), 1):
    # igual a fazer => for i in [0, 1, 2, 3]:
    print(f"Produto {i}: {mercado[i]}")
print(i)

# mesmo loop usando WHILE
i = 0
while i<len(mercado):
    print(f"Produto {i}: {mercado[i]}")
    i += 1
print(i)

convidados = [] # lista vazia
print(convidados)
nome = input("Nome do convidado ('fim' para terminar): ")
while nome != 'fim':
    convidados.append(nome) # adiciona ao final da lista
    nome = input("Nome do convidado ('fim' para terminar): ")
print("Convidados para a festa: ", convidados)

# loop for each, objetivo é pegar o conteudo (nao posicao)
print("Para comprar: ", end="") # evitar pular a linha
for item in mercado:
    print(f"{item}", end=", ")

# bricando com alguns métodos da classe list
# que é uma lista dinâmica 
# olhar em: https://www.w3schools.com/python/python_lists_methods.asp
print()
print(mercado)
mercado.append("acelga")
mercado.append("cebola")
print(mercado)
mercado.sort()
print(mercado)
mercado.reverse()
print(mercado)

vet1 = [1, 3, 5, 7, 9]
vet2 = [0]*10
vet3 = []
print(f"Vetor: {vet1}, comprimento: {len(vet1)}")
print(f"Vetor: {vet2}, comprimento: {len(vet2)}")
print(f"Vetor: {vet3}, comprimento: {len(vet3)}")
'''

# Aula 4 - Intro a listas e Intro a matriz
'''
# matriz é lista de listas
# neste caso, duas listas (duas linhas)
# de 3 elementos (3 colunas), ou seja, 2x3
m1 = [[1, 2, 3], 
      [4, 5, 6]] 
print(m1) # imprime toda a matriz
print(m1[0]) # imprime toda a sublista 0 (linha 0)
print(m1[0][0]) # imprime primeiro elemento (0,0)

print("Linhas: ", len(m1)) # total de linhas da matriz
print("Colunas: ", len(m1[0])) # total de colunas da matriz

# loop duplo usando o valor FIXO da LINHA e COLUNA
for i in range(2):  # loop da linha: 0, 1 
    for j in range(3):  # loop da coluna: 0, 1 e 2
        print(f"[{i}][{j}] ", end=" ")
    print()

# loop duplo usando LEN para saber total de linhas/colunas
# assim, fica genérica para tamanhos diferentes
for i in range(len(m1)):   
    for j in range(len(m1[i])): 
        print(f"{m1[i][j]} ", end=" ")
    print()

m2 = [[1],  # exemplo de lista de lista
      [2, 3.6],  # matriz em que cada linha
      [4, 5, True],  # tem um total de coluna diferente
      ['0', "tchau"], 
      [3.2, 4.5]]
print("---> ", m2[3][1][2])
for i in range(len(m2)):   
    for j in range(len(m2[i])): 
        print(f"{m2[i][j]} ", end=" ")
    print()

print(m2)

m3 = [0]*5
print(m3)
for i in range(len(m3)):
    m3[i] = [i]*5
    print(m3)
'''
    
# Aula 5 - Matriz 2 e My mat
'''

from my_mat import ler_matriz, imprimir_matriz, criar_matriz

lin = int(input("Quantas linhas? "))
col = int(input("Quantas colunas? "))
mu = ler_matriz(lin, col)
imprimir_matriz(mu)

x = criar_matriz(20, 20, -1)
imprimir_matriz(x)


'''

# Aula 6 - Matriz 3, My mat functions and My mat util
'''

from my_mat_util import ler_matriz, imprimir_matriz, ler_dimensao
from my_mat_functions import criar_matriz

la, ca = ler_dimensao("Matriz A")
ma = ler_matriz(la, ca)
imprimir_matriz(ma)

lb, cb = ler_dimensao("Matriz B")
mb = ler_matriz(lb, cb)
imprimir_matriz(mb)

if ca != lb:
    print(f"Não é possível multiplicar, coluna {ca} diferente de linha {lb}")
else: # posso calcular matriz mr
    mr = criar_matriz(la, cb)
    for i in range(la):
        for j in range(cb):
            for k in range(ca):
                mr[i][j] = mr[i][j] + ma[i][k] * mb[k][j]

print("Matriz resultado da multiplicação: ")
imprimir_matriz(mr)

'''

# Atividade - Fibonacci
'''
tam_seq = int(input("Escreva o tamanho da sequencia desejada:"))
anterior = 0
atual = 1
futuro = 0
i = 0
while i < tam_seq:
    
    print(atual)
    
    futuro = anterior + atual
    anterior = atual
    atual = futuro

    i = i + 1

print('Isso é Fibonacci!')
'''

# Aula 7 - vamo vê
