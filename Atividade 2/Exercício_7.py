# Exercício 07:

sal = float(input("Digite o salário atual: $ "))
aum = float(input("Digite o percentual de aumento (%): "))

adi = sal * (aum / 100)
novo = adi + sal

print("Seu novo salário é de R${:.2f}." .format(novo))