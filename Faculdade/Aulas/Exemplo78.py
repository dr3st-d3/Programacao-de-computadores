# Exemplo 78 - exemplo de método com parâmetro (função)

def somaDoisValores(a, b):
    a = a + b
    return a

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
print(somaDoisValores(a, b))
print(a)
