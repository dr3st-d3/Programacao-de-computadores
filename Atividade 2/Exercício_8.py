# Exercício 08:

h1 = float(input("Qual é o valor da altura do retângulo? "))
b1 = float(input("Qual o valor da base do retângulo? "))

per = h1 + h1 + b1 + b1
area = h1 * b1

print("Certo.\nO perímetro do retângulo é {}.\nE a área é {:.2f}." .format(per, area))
