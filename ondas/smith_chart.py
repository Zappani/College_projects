"""
Trabalho da matéria de propagação de ondas

Lucas Zappani Siqueira 
GRR 20202599
2024

Referências:
https://www.feis.unesp.br/Home/departamentos/engenhariaeletrica/optoeletronica/capitulo-6---metodos-graficos-em-lt-loe.pdf
https://wiki.sj.ifsc.edu.br/images/8/8a/TCC290_Paula_Cristina_Grando.pdf
"""

def complex_input(prompt):
    """
    Solicita ao usuário um número complexo no formato a+bj.
    Em caso de erro na entrada, informa o usuário e solicita a entrada novamente.
    
    Parâmetros:
    prompt (str): A mensagem de solicitação para a entrada do usuário.
    
    Retorna:
    complex: O número complexo inserido pelo usuário.
    """
    try:
        return complex(input(prompt))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número complexo na forma a+bj.")
        return complex_input(prompt)

def impedancia_normalizada(Z, Z0):
    """
    Calcula a impedância normalizada.
    
    Parâmetros:
    Z (complex): A impedância da carga.
    Z0 (complex): A impedância característica.
    
    Retorna:
    complex: A impedância normalizada.
    """
    return Z / Z0

def coeficiente_reflexao(Z, Z0):
    """
    Calcula o coeficiente de reflexão.
    
    Parâmetros:
    Z (complex): A impedância da carga.
    Z0 (complex): A impedância característica.
    
    Retorna:
    complex: O coeficiente de reflexão.
    """
    return (Z - Z0) / (Z + Z0)

def main():
    """
    Função principal do programa. Solicita ao usuário as impedâncias Z0 e ZL, calcula e exibe
    a impedância normalizada e o coeficiente de reflexão, além de suas partes real e imaginária.
    """
    Z0 = complex_input("Insira a impedância característica Z0 (por exemplo, 50+0j): ")
    ZL = complex_input("Insira a impedância da carga ZL (por exemplo, 100+50j): ")

    ZL_normalizado = impedancia_normalizada(ZL, Z0)
    gama = coeficiente_reflexao(ZL, Z0)
    modulo_gama = abs(gama)
    parte_real_gama = gama.real
    parte_imaginaria_gama = gama.imag

    print(f"Impedância normalizada (zL): {ZL_normalizado}")
    print(f"Coeficiente de reflexão (Γ): {gama}")
    print(f"Módulo do coeficiente de reflexão (|Γ|): {modulo_gama}")
    print(f"Parte real do coeficiente de reflexão (|ΓRe|): {parte_real_gama}")
    print(f"Parte imaginária do coeficiente de reflexão (|ΓIm|): {parte_imaginaria_gama}")

    while True:
        if input("Pressione Enter para encerrar o programa") == "":
            break

if __name__ == "__main__":
    main()
