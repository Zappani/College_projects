from my_mat_functions import criar_matriz

# imprime matriz com jeitão de matriz
def imprimir_matriz(m):

    for i in range(len(m)):  # total de linhas
        for j in range(len(m[i])):  # total de colunas
            print(f"{m[i][j]:^} ", end=" ")
        print()

# criar e depois lê uma matriz (linhas x colunas)
def ler_matriz(nome, linhas, colunas):
    print(f"Dados da matriz {nome}:")
    m = criar_matriz(linhas, colunas)
    for i in range(len(m)):  
        for j in range(len(m[i])):  
            m[i][j] = int(input(f"   - celula [{i}][{j}]: "))
    return m

# le as dimensões (linha e coluna) e retorna como tupla
def ler_dimensao(nome):
    print(f"Para a {nome}, qual a dimensão?")
    lin = int(input("   - quantidade de linhas: "))
    col = int(input("   - quantidade de colunas: "))
    return lin, col # retorna uma tupla
