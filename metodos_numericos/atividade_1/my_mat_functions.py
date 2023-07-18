# cria e retorna uma matriz (linhas x colunas) com conteúdo celula (ou zero por default)
def criar_matriz(linhas, colunas, celula=0):
    m = [0]*linhas
    for i in range(len(m)):
        m[i] = [celula]*colunas
    return m

# cria e retorna uma matriz identidade
def criar_identidade(dimensao):
    m = criar_matriz(dimensao, dimensao)
    # for para colocar 1 na diagonal principal
    for linha in range(dimensao):
        m[linha][linha] = 1
    return m

# multiplica duas matrizes e retorna uma matriz resultado
def multiplica_matrizes(ma, mb):
    la = len(ma)
    ca = len(ma[0])
    cb = len(mb[0])
    mr = criar_matriz(la, cb)
    for i in range(la):
        for j in range(cb):
            for k in range(ca):
                mr[i][j] = mr[i][j] + ma[i][k] * mb[k][j]
    return mr

# gera a transposta de uma matriz
def transpoe_matrizes(m):
    
    c = len(m)
    l = len(m[0])
    mt = criar_matriz(l, c) 
    
    for i in range(len(mt)):
        #imprimir_matriz(mt)
        for j in range(len(mt[0])):
            mt[i][j] = m[j][i]
            #imprimir_matriz(mt)

    return mt

# multiplica uma matriz por um numero escalar qualquer k
def multip_escalar(m, k):
    l = len(m)
    c = len(m[0])

    mk = criar_matriz(l, c) 
    
    for i in range(len(mk)):
        for j in range(len(mk[0])):
            mk[i][j] = m[i][j]*k 
            
    return mk

# calcula o maior, o menor e a soma dos elementos da matriz
def mms(m):

    a = soma(m)
    b = maior(m)
    c = menor(m)

    print(f'Soma:{a},\nMenor:{c}, \nMaior:{b}.')
    
    return 0

# função auxiliar para calcular o maior valor da matriz
def maior(m):

    maior = m[0][0]
    for i in range(len(m)): # faz a soma dos valores da matriz
        for j in range(len(m[0])):
            if maior < m[i][j]:
                maior = m[i][j]

    return maior

# função auxiliar para calcular o menor valor da matriz
def menor(m):

    menor = m[0][0]
    for i in range(len(m)): # faz a soma dos valores da matriz
        for j in range(len(m[0])):
            if menor > m[i][j]:
                menor = m[i][j]

    return menor

# função auxiliar para calcular a soma valor da matriz
def soma(m):

    soma = 0

    for i in range(len(m)): # faz a soma dos valores da matriz
        for j in range(len(m[0])):
            
            soma = soma + m[i][j]

    return soma

# encontra a determinante de uma matriz 3x3 com a propriedade de Sarrus
def determinante_3x3(m):
    
    det1 = m[0][0]*m[1][1]*m[2][2]
    det2 = m[0][1]*m[1][2]*m[2][0]
    det3 = m[0][2]*m[1][0]*m[2][1]
    det4 = m[0][1]*m[1][0]*m[2][2]
    det5 = m[0][0]*m[1][2]*m[2][1]
    det6 = m[0][2]*m[1][1]*m[2][0]

    det = det1 + det2 + det3 - det4 - det5 - det6

    return det

# encontra a determinante de uma matriz 4x4 com a propriedade de Laplace
def determinante_4x4(m):
    
    deta = m[0][0]*(  
        m[1][1]*m[2][2]*m[3][3] 
        +m[1][2]*m[2][3]*m[3][1]
        +m[1][3]*m[2][1]*m[3][2]
        -m[1][2]*m[2][1]*m[3][3]
        -m[1][1]*m[2][3]*m[3][2]
        -m[1][3]*m[2][2]*m[3][1])
    
    detb = m[1][0]*(

        m[0][1]*m[2][2]*m[3][3] 
        +m[0][2]*m[2][3]*m[3][1]
        +m[0][3]*m[2][1]*m[3][2]
        -m[0][2]*m[2][1]*m[3][3]
        -m[0][1]*m[2][3]*m[3][2]
        -m[0][3]*m[2][2]*m[3][1])
     
    detc = m[2][0]*(

        m[0][1]*m[1][2]*m[3][3] 
        +m[0][2]*m[1][3]*m[3][1]
        +m[0][3]*m[1][1]*m[3][2]
        -m[0][2]*m[1][1]*m[3][3]
        -m[0][1]*m[1][3]*m[3][2]
        -m[0][3]*m[1][2]*m[3][1])
     
    detd = m[3][0]*(
        m[0][1]*m[1][2]*m[2][3] 
        +m[0][2]*m[1][3]*m[2][1]
        +m[0][3]*m[1][1]*m[2][2]
        -m[0][2]*m[1][1]*m[2][3]
        -m[0][1]*m[1][3]*m[2][2]
        -m[0][3]*m[1][2]*m[2][1])
    
    det = deta -detb +detc -detd
    return det
 
# faz a inversa de uma matriz 3x3
def inversa_3x3(m):
    det = determinante_3x3(m)

    inv = criar_matriz(3,3)

    if det == 0:
        print("Determinante igual a 0, impossivel encontrar a inversa")
    else:
        inv[0][0] = (m[1][1]*m[2][2]-m[1][2]*m[2][1])/det
        inv[0][1] = (m[2][1]*m[0][2]-m[2][2]*m[0][1])/det
        inv[0][2] = (m[0][1]*m[1][2]-m[1][1]*m[0][2])/det
        inv[1][0] = (m[1][2]*m[2][0]-m[2][2]*m[1][0])/det
        inv[1][1] = (m[2][2]*m[0][0]-m[2][0]*m[0][2])/det
        inv[1][2] = (m[0][2]*m[1][0]-m[0][0]*m[1][2])/det
        inv[2][0] = (m[1][0]*m[2][1]-m[1][1]*m[2][0])/det
        inv[2][1] = (m[2][0]*m[0][1]-m[2][1]*m[0][0])/det
        inv[2][2] = (m[0][0]*m[1][1]-m[0][1]*m[1][0])/det
    
    return inv

