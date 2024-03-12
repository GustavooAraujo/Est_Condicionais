num_1 = float(input("Escolha seu primeiro número:"))
num_2 = float(input("Escolha seu segundo número:"))
operacao = input("Qual operação deseja realizar (+, -, *, /)?")

# Executando as operações matemáticas conforme a selecionado.
if operacao =="+":
    resultado = num_1 +num_2
elif operacao == "-":
    resultado = num_1 - num_2
elif operacao == "*":
    resultado = num_1 * num_2
elif operacao == "/":
    resultado = num_1 / num_2

#  Verificando os dados atribuídos anteriormente.
if resultado % 1 == 0:
    print("O resultado é um número inteiro.")
else:
    print("O resultado foi um número decimal.")

if resultado > 0:
    print("O resultado é positivo.")
elif resultado == 0:
    print("O resultado é neutro.")
else:
    print("O resultado é negativo.")

if resultado % 2 == 0:
    print("O resultado é par.")
else:
    print("O resultado é impar.")