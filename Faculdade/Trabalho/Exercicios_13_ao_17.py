#Exercício - 13

fun = input("\nQual função (+, - , *, / ) deseja usar? ")
n1 = float(input("\nDigite o 1° valor: "))
n2 = float(input("\nDigite o 2° valor: "))

if fun == '+':
    resultado = n1 + n2
    print("\n%2d + %2d = %2d" %(n1,n2,resultado))

elif fun == '-':
    resultado = n1 - n2
    print("\n%2d - %2d = %2d" %(n1,n2,resultado))

elif fun == '*':
    resultado = n1 * n2
    print("\n%2d * %2d = %2d" %(n1,n2,resultado))

elif fun == '/':
    
    if n1 == 0:
        print("\nDivisão por zero não é possível.")
    
    elif n2 == 0:
        print("\nDivisão por zero não é possível.")
    
    else:
        resultado = n1 / n2
        print("\n%2d / %2d = %2d" %(n1,n2,resultado))

#Exercício - 14

kw = float(input("\nDigite quantos kWh foram consumidos: "))

if kw < 0:
    print("Valor inválido, tente novamente.")

tipo = input("\nDigite o tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ")

if tipo == 'R':
    preco = 0.40 if kw <= 500 else 0.65
    
elif tipo == 'C':
    preco = 0.55 if kw <= 1000 else 0.60
    
elif tipo == 'I':
    preco = 0.55 if kw <= 5000 else 0.60
    
else:
    print("Erro: Tipo de instalação inválido. Use R, C ou I.")

cal = kw * preco
print("\nO valor a pagar é R$%2d." %(cal))

#Exercício - 15

valor = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o valor do seu salário mensal: R$ "))
anos = int(input("Digite a quantidade de anos para pagar: "))

if valor <= 0 or salario <= 0 or anos <= 0:
    print("Valor inválido.")

meses = anos * 12
prestacao = valor / meses
limite = salario * 0.30

print("Valor da prestação: R$%2f" %(prestacao))
print("Limite máximo: R$%2f" %(limite))

if prestacao <= limite:
    print("Empréstimo Aprovado.")
else:
    print("Empréstimo Negado, A prestação excede o limite.")

#Exercício - 16

import math

area = float(input("Digite o tamanho da área a ser pintada: "))

if area <= 0:
    print("Valor inválido.")
    
l = area / 3
latas = math.ceil(l / 18)
total = latas * 80.0

print("Você precisará de %2f lata(s) de tinta." %(latas))
print("Preço total: R$%2f" %(total))

#Exercício - 17

for numero in range(0, 101, 2):
    print(numero)
