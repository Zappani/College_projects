def complex_input(prompt):
    try:
        return complex(input(prompt))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número complexo na forma a+bj.")
        return complex_input(prompt)

def impedancia_normalizada(Z, Z0):
    return Z / Z0

def coeficiente_reflexao(Z, Z0):
    return (Z - Z0) / (Z + Z0)

def main():
    Z0 = complex_input("Insira a impedância característica Z0 (por exemplo, 50+0j): ")
    ZL = complex_input("Insira a impedância da carga ZL (por exemplo, 100+50j): ")

    ZL_normalizado = impedancia_normalizada(ZL, Z0)
    gama = coeficiente_reflexao(ZL, Z0)
    modulo_gama = abs(gama)
    parte_real_gama = gama.real
    parte_imaginaria_gama = gama.imag

    print(f"Impedância normalizada (zL): {ZL_normalizado}")
    print(f"Coeficiente de reflexão (Γ): {gama}")
    print(f"Módulo do coeficiente de reflexão (|ΓL|): {modulo_gama}")
    print(f"Parte real do coeficiente de reflexão (|ΓRe|): {parte_real_gama}")
    print(f"Parte imaginária do coeficiente de reflexão (|ΓIm|): {parte_imaginaria_gama}")

    while True:
        if input("Pressione Enter para encerrar o programa") == "":
            break
            


if __name__ == "__main__":
    main()
