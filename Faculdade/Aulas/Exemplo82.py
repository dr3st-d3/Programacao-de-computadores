# Exemplo 82 - cálculo da área de um triângulo

def calculoArea(base, altura):
    area = base * altura / 2
    return(area)

base = float(input("Digite a base do triângulo em cm: "))
altura = float(input("Digite a altura do triângulo em cm: "))
print("A área do triângulo é %.2f cm²" %(calculoArea(base, altura)))

print(calculoArea(8,5))
print(calculoArea(10,10))
print(calculoArea(2,5))
