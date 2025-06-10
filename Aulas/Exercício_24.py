# Exemplo 24 - cálculo do IMC - if-elif-else
import math

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em m: "))
imc = peso / math.pow(altura, 2)
print("\nO valor do IMC é %.2f" %(imc))

if imc < 20:
    print("\nAbaixo do peso.")
elif imc >= 20 and imc < 25:
    print("\nPeso normal.")
elif imc >= 25 and imc < 30:
    print("\nSobrepeso.")
elif imc >= 30 and imc < 40:
    print("\nObeso.")
elif imc >= 40:
    print("\nObeso mórbido.")
    