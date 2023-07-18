import numpy as np

def titulo(titulo=''):# Função para imprimir o cabeçalho com título formatado
    print(f'\n{titulo:*^50}')

def opcoes():# Função para mostrar as opções do menu  
    print('1-> Calcular área da função f(x) = x^2 - 2x + 8')
    print('2-> Calcular área do polinômio')
    print('0-> Sair')

def opcao_menu():
    menu = int(input('-> Opção: '))

    return menu

def ler_coef():# Função para ler os coeficientes de um polinômio
    grau = int(input('-> Grau do polinômio: '))
    coef = np.zeros(grau+1)

    for i in range(len(coef)-1, -1, -1):
        if i > 0:
            coef[i] = float(input(f'-> Coeficiente de x^{i}: '))
        else:
            coef[i] = float(input(f'-> Termo independente: '))

    return coef

def imprimi_poli(coef):# Função para imprimir a expressão da função polinomial
    print('[>] f(x) = ', end='')

    for i in range(len(coef)-1, -1, -1):
        if i > 1:
            if coef[i] >= 0:
                print(f'{coef[i]}x^{i} + ', end='')
            else:
                print(f'({coef[i]})x^{i} + ', end='')
        elif i == 1:
            if coef[i] >= 0:
                print(f'{coef[i]}x + ', end='')
            else:
                print(f'({coef[i]})x + ', end='')
        else:
            if coef[i] >= 0:
                print(f'{coef[i]}')
            else:
                print(f'({coef[i]})')

def ler_lim():# Função para ler os limites da soma
    inf = float(input('-> Limite inferior: '))
    sup = float(input('-> Limite superior: '))

    return inf, sup

def ler_passo():# Função para ler o passo da soma
    passo = float(input('-> Passo da soma: '))
    return passo
    
def info_polinomio(coef, inf, sup, passo):
    titulo(' Dados do polinômio ')
    imprimi_poli(coef)
    print(f'[>] Limites de integração: [{inf}, {sup}]')
    print(f'[>] Passo da soma: [{passo}]')
