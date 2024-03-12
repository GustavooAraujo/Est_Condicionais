print("Aqui iremos coletar os lados do triângulo.")
lado_1 = float(input("Digite aqui o comprimento do primeiro lado:"))
lado_2 = float(input("Digite aqui o comprimento do segundo lado:"))
lado_3 = float(input("Digite aqui o comprimento do terceiro lado:"))

if (lado_1 + lado_2 > lado_3) and (lado_2 + lado_3 > lado_1) and (lado_1 + lado_3 > lado_2):
    print("O valores podem formar um triângulo.")
    # Verificando o tipo de triângulo.
    if (lado_1 == lado_2) and (lado_2 == lado_3):
        print("O triângulo é equilátero.")
    elif (lado_1 != lado_2) and (lado_2 != lado_3) and (lado_1 != lado_3):
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")
else:
    print("Os valores não formam um triângulo.")