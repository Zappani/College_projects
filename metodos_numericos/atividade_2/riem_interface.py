# TE327 - Métodos Numéricos 
# Trabalho 2 - Soma de Riemann
# Prof. Dr. Henri Frederico Eberspacher
# Aluno: Lucas Zappani Siqueira - GRR20202599 

import numpy as np
import matplotlib.pyplot as plt
import riem_func as func
import riem_utils as util

def calc_area():# Calcula a área da função B fornecida  
    util.titulo(' Área da função f(x) = x^2 - 2x + 8 ')

    # Dados do polinômio
    coef = np.array([8, -2, 1])
    inf, sup = (-4, 4)
    passo = util.ler_passo()
    passo_func = 0.03125
    area_int = 320/3
    
    # Garantindo uma precisão mínima da curva da função
    # Passo <= 1/32
    if passo/4 < passo_func:
        passo_func = passo/4
    
    # Imprimindo os dados do polinômio
    util.info_polinomio(coef, inf, sup, passo) 
    
    # Plot da soma pela esquerda
    plt.subplot(1, 3, 1)
    func.plot_func( inf, sup, passo_func)
    area_esq = func.soma_esquerda( inf, sup, passo)
    erro_esq = abs(area_int-area_esq)/area_int*100
    plt.title(f'Soma pela esquerda: {area_esq}\n'
              f'Área da integral: {area_int}\n'
              f'Erro relativo: {erro_esq}%')
    plt.xlabel(f'Passo: {passo}')
    
    # Plot da soma pelo centro
    plt.subplot(1, 3, 2)
    func.plot_func( inf, sup, passo_func)
    area_cen = func.soma_centro( inf, sup, passo)
    erro_cen = abs(area_int-area_cen)/area_int*100
    plt.title(f'Soma pelo centro: {area_cen}\n'
              f'Área da integral: {area_int}\n'
              f'Erro relativo: {erro_cen}%')
    plt.xlabel(f'Passo: {passo}')
    
    # Plot da soma pela direita
    plt.subplot(1, 3, 3)
    func.plot_func( inf, sup, passo_func)
    area_dir = func.soma_direita( inf, sup, passo)
    erro_dir = abs(area_int-area_dir)/area_int*100
    plt.title(f'Soma pela direita: {area_dir}\n'
              f'Área da integral: {area_int}\n'
              f'Erro relativo: {erro_dir}%')
    plt.xlabel(f'Passo: {passo}')
    
    # Mostrando o plot finalizado
    plt.show()

def calcular_area_polinomio():# Calcula a área do polinômio
    util.titulo(' Área do polinômio ')
    
    # Dados do polinômio
    coef = util.ler_coef()
    inf, sup = util.ler_lim()
    passo = util.ler_passo()
    
    # Garantindo uma precisão mínima da curva da função
    # Passo <= 1/32
    passo_func = 0.03125
    if passo/4 < passo_func:
        passo_func = passo/4
    
    # Imprimindo os dados do polinômio
    util.info_polinomio(coef, inf, sup, passo)
    
    # Plot da soma pela esquerda
    plt.subplot(1, 3, 1)
    func.plotar_polinomio(coef, inf, sup, passo_func)
    area_esq = func.soma_esq_pol(coef, inf, sup, passo)
    plt.title('Soma pela esquerda\n'
              f'Área estimada: {area_esq}')
    plt.xlabel(f'Passo: {passo}')
    
    # Plot da soma pelo centro
    plt.subplot(1, 3, 2)
    func.plotar_polinomio(coef, inf, sup, passo_func)
    area_cen = func.soma_cent_pol(coef, inf, sup, passo)
    plt.title('Soma pelo centro\n'
              f'Área estimada: {area_cen}')
    plt.xlabel(f'Passo: {passo}')
    
    # Plot da soma pela direita
    plt.subplot(1, 3, 3)
    func.plotar_polinomio(coef, inf, sup, passo_func)
    area_dir = func.soma_dir_pol(coef, inf, sup, passo)
    plt.title('Soma pela direita\n'
              f'Área estimada: {area_dir}')
    plt.xlabel(f'Passo: {passo}')
    
    # Mostrando o plot finalizado
    plt.show()

menu = 1# Variável de opções do menu

while menu != 0:# Menu do programa
    util.titulo(' Soma de Riemann ')
    util.opcoes()
    menu = util.opcao_menu()
    
    if menu == 1:
        calc_area()
    elif menu == 2:
        calcular_area_polinomio()
