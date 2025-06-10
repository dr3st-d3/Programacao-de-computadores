# Exercício 09:

preço = float(input("Digite o preço do produto: R$"))
percentual = float(input("Digite o desconto para o pagamento à vista (%): "))

desconto = preço * (percentual / 100)
preçof = preço - desconto

print("O preço do produto com o desconto aplicado é de R${:.2f}." .format(preçof))