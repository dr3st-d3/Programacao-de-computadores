# Exemplo 75 - lucro de uma empresa

faturamento = float(input("Digite o faturamento em :R$ "))
custo = float(input("Digite o custo em :R$ "))
lucro = faturamento - custo
lucro = f"R$ {lucro:_.2f}"
lucro = lucro.replace('.',',').replace('_','.')
print(f"O lucro foi de R$ {lucro}")
