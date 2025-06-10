# Exemplo 79 - exemplo de método

def somaDoisValores(a, b):
    result = a + b
    return result

x = float(input("Digite o 1º número: "))
y = float(input("Digite o 2º número: "))
print("A soma dos valores é %.2f" %(somaDoisValores(x, y)))
