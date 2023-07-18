import numpy as np
import matplotlib.pyplot as plt

def func_i(x):# Função para calcular o y da função B
    y = x**2 - 2*x + 8
    return y

def plot_func( inf, sup, passo=0.03125):# Função para plotar a curva da função A ou B
                                             # Passo padrão = 1/32 = 0.03125

    vec_x = np.arange(inf, sup+passo/2, passo)
    vec_y = np.zeros(len(vec_x))
    for i in range(len(vec_y)):
        vec_y[i] = func_i(vec_x[i])
    plt.plot(vec_x, vec_y, color='blue')

def soma_esquerda( inf, sup, passo):# Função para calcular a soma de Riemann pela esquerda da função A ou B
    soma = 0
    x_var = inf
    y_var = 0

    for i in range(round((sup-inf)/passo)):
        y_var = func_i(x_var)
        plt.plot(x_var, y_var, marker='o', color='blue')
        plt.bar(x_var, y_var, passo, align='edge')
        soma += passo * y_var
        x_var += passo

    print(f'[>] Soma pela esquerda = {soma}')
    return soma

def soma_centro( inf, sup, passo):# Função para calcular a soma de Riemann pelo centro da função A ou B
    soma = 0
    x_var = inf
    y_var = 0

    for i in range(round((sup-inf)/passo)):
        y_var = func_i(x_var+passo/2)
        plt.plot(x_var+passo/2, y_var, marker='o', color='blue')
        plt.bar(x_var, y_var, passo, align='edge')
        soma += passo * y_var
        x_var += passo

    print(f'[>] Soma pelo centro = {soma}')
    return soma

def soma_direita( inf, sup, passo):# Função para calcular a soma de Riemann pela direita da função A ou B
    soma = 0
    x_var = inf
    y_var = 0

    for i in range(round((sup-inf)/passo)):
        y_var = func_i(x_var+passo)
        plt.plot(x_var+passo, y_var, marker='o', color='blue')
        plt.bar(x_var, y_var, passo, align='edge')
        soma += passo * y_var
        x_var += passo

    print(f'[>] Soma pela direita = {soma}')
    return soma

def plotar_polinomio(coef, inf, sup, passo=0.03125):# Função para plotar a curva da função polinomial
                                                    # Passo padrão = 1/32 = 0.03125
    vec_x = np.arange(inf, sup+passo/2, passo)
    vec_y = np.zeros(len(vec_x))

    for i in range(len(vec_y)):
        vec_y[i] = polinomio(coef, vec_x[i])
    plt.plot(vec_x, vec_y, color='blue')

def polinomio(coef, x):# Função para calcular o y da função polinomial
    y = 0

    for i in range(len(coef)):
        y += coef[i] * x**i
    return y    

def soma_esq_pol(coef, inf, sup, passo):# Função para calcular a soma de Riemann pela esquerda da função polinomial
    soma = 0
    x_var = inf
    y_var = 0

    for i in range(round((sup-inf)/passo)):
        y_var = polinomio(coef, x_var)
        plt.plot(x_var, y_var, marker='o', color='blue')
        plt.bar(x_var, y_var, passo, align='edge')
        soma += passo * y_var
        x_var += passo

    print(f'[>] Soma pela esquerda = {soma}')
    return soma

def soma_cent_pol(coef, inf, sup, passo):# Função para calcular a soma de Riemann pelo centro da função polinomial
    soma = 0
    x_var = inf
    y_var = 0
    
    for i in range(round((sup-inf)/passo)):
        y_var = polinomio(coef, x_var+passo/2)
        plt.plot(x_var+passo/2, y_var, marker='o', color='blue')
        plt.bar(x_var, y_var, passo, align='edge')
        soma += passo * y_var
        x_var += passo

    print(f'[>] Soma pelo centro = {soma}')
    return soma

def soma_dir_pol(coef, inf, sup, passo):# Função para calcular a soma de Riemann pela direita da função polinomial
    soma = 0
    x_var = inf
    y_var = 0

    for i in range(round((sup-inf)/passo)):
        y_var = polinomio(coef, x_var+passo)
        plt.plot(x_var+passo, y_var, marker='o', color='blue')
        plt.bar(x_var, y_var, passo, align='edge')
        soma += passo * y_var
        x_var += passo

    print(f'[>] Soma pela direita = {soma}')
    return soma
