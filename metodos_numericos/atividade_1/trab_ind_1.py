from my_mat_util import ler_matriz, imprimir_matriz, ler_dimensao
from my_mat_functions import criar_identidade, multiplica_matrizes, transpoe_matrizes, multip_escalar, determinante_3x3, determinante_4x4, inversa_3x3, mms

def identidade():
    print("-- Identidade --\n")
    li, ci  = ler_dimensao("Matriz Identidade")
    if li != ci:
        print("\n   Identidade apenas para matrizes quadradas!")
    else:
        mi = criar_identidade(li)
        imprimir_matriz(mi)

def mult():
    print("-- Multiplicar Matrizes --\n")
    la, ca = ler_dimensao("Matriz A")
    lb, cb = ler_dimensao("Matriz B")
    if ca != lb:
        print(f"Não é possível multiplicar, coluna {ca} diferente de linha {lb}")
    else: # posso calcular matriz mr
        ma = ler_matriz("Matriz A", la, ca)
        imprimir_matriz(ma)
        mb = ler_matriz("Matriz B", lb, cb)
        imprimir_matriz(mb)
        mr = multiplica_matrizes(ma, mb)
        print("Matriz resultado da multiplicação: ")
        imprimir_matriz(mr)

def transposta():

    print("-- Transposta --\n")
    l, c  = ler_dimensao("Matriz escolhida")
    m = ler_matriz("Matriz escolhida", l, c)

    print("Matriz escolhida:")
    imprimir_matriz(m)

    print("Transposta da matriz escolhida:")
    mt = transpoe_matrizes(m)
    imprimir_matriz(mt)
  
def mult_escalar():
    
    print("-- Multiplicação escalar --\n")
    l, c  = ler_dimensao("Matriz escolhida")
    m = ler_matriz("Matriz escolhida", l, c)

    print("Matriz escolhida:")
    imprimir_matriz(m)
    k = int(input("Escalar a ser multiplicado:"))

    mm = multip_escalar(m, k)

    print("Matriz final:")

    imprimir_matriz(mm)

def mai_men_soma():

    print("-- Maior, menor e soma dos componentes da matriz --\n")
    l, c  = ler_dimensao("Matriz escolhida")
    m = ler_matriz("Matriz escolhida", l, c)

    print("Matriz escolhida:")
    imprimir_matriz(m)
    print()

    mms(m)

def det_3x3():

    print("-- Determinante matriz 3x3 --\n")
    l, c  = 3, 3
    m = ler_matriz("escolhida", l, c)

    print("Matriz escolhida:")
    imprimir_matriz(m)

    print("Determinante da matriz escolhida:")
    det = determinante_3x3(m)

    print(det)
    
def det_4x4():
    
    print("-- Determinante matriz 4x4 --\n")
    l, c  = 4, 4
    m = ler_matriz("Matriz escolhida", l, c)

    print("Matriz escolhida:")
    imprimir_matriz(m)

    print("Determinante da matriz escolhida:")
    mt = determinante_4x4(m)
    print(mt)

def inv_3x3():
    
    print("-- Inversa matriz 3x3 --\n")
    l, c  = 3, 3
    m = ler_matriz("Matriz escolhida", l, c)

    print("Matriz escolhida:")
    imprimir_matriz(m)

    print("Inversa da matriz escolhida:")
    inv = inversa_3x3(m)
    imprimir_matriz(inv)

opcao = 1

while opcao != 0:
    print("\n-- Menu --\n")
    print("0 - sair")
    print("1 - criar identidade")
    print("2 - multiplicar matrizes")
    print("3 - transposta de matriz")
    print("4 - multiplicar matriz por escalar")
    print("5 - Calcula o maior, o menor e a soma dos elementos da matriz")
    print("6 - determinante de matriz (3x3)")
    print("7 - determinante de matriz (4x4)")
    print("8 - calcular matriz inversa (3x3)")

    opcao = int(input("Qual sua opcão: "))

    if opcao == 1:
        identidade()
        opcao = 0
    elif opcao == 2:
        mult()
        opcao = 0
    elif opcao == 3:
        transposta()
        opcao = 0
    elif opcao == 4:
        mult_escalar()
        opcao = 0
    elif opcao == 5:
        mai_men_soma()
        opcao = 0
    elif opcao == 6:
        det_3x3()
        opcao = 0
    elif opcao == 7:
        det_4x4()
        opcao = 0
    elif opcao == 8:
        inv_3x3()
        opcao = 0