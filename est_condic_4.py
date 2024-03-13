# coletando a quantidade de litros e o tipo de combústivel
#Colocando tudo pra maiúscula para facilitar a análise.
quant_litros = float(input("Quanto litros foram vendidos ?"))
tipo_combustivel = input("E (etanol) / D (Dísel) ").upper()

# Verificando o tipo de combústivel
if tipo_combustivel == "E":
    preco_litro = 1.70 # Taxamos o preco etanol nos dado.
    if quant_litros <= 15:
        desconto = 0.02 # desconto sugerido no enunciado.
    else:
        desconto = 0.04
elif tipo_combustivel == "D":
    preco_litro = 2.00 #  Taxamos o preco dísel nos dado.
    if quant_litros <= 15:
        desconto = 0.03 # desconto sugerido no enunciado.
    else:
        desconto = 0.05
# Caso ocorra um erro na especificação de tipo de combustível,
# Consideramos entradas inválidas, e os preços são taxados em 0.

else: # Entradas inválidas
    preco_litro = 0
    desconto = 0

# Memória do valor do desconto e do preço descontado
valor_descont = preco_litro * quant_litros * desconto
valor_pago = preco_litro * quant_litros - desconto