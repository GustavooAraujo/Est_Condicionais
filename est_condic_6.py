vendas_2022 = float(input("Qaunto foi as vendas de 2022: "))
vendas_2023 = float(input("Qaunto foi as vendas de 2023: "))

# Cálculo de variação em percentual entre as vendas dos anos de 2022 e 2023.
var_percentual = (vendas_2023 - vendas_2022) / (vendas_2022) * 100

# Análise condicional da variação percentual para determinar a sugestão a ser enviada.
if var_percentual > 20:
    print("Bônus pra o timme de vendas.")
elif 2 <= var_percentual <= 20:
    print("Pequena bonificação para o time de vendas.")
elif -10 <= var_percentual < 2:
    print("Planejamento de políticas de incentivos às vendas.")
else:
    print("Corte todos os custos!")