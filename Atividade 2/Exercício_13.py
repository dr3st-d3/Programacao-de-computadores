# Exercício 13:

gasto = float(input("Digite o valor gasto no restaurante: R$ "))

gorjeta = gasto * 0.10
total = gasto + gorjeta

print("O valor total a ser pago é de R${:.2f}.\nObrigado por frequentar o restaurante ComaBem!!\nVolte sempre." .format(total))
