# Exercício 11:

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    r1 = (-b + math.sqrt(delta)) / (2*a)
    r2 = (-b - math.sqrt(delta)) / (2*a)

print("O resultado das raizes é:")
print("1° raiz: {:.2f}" .format(r1))
print("2° raiz: {:.2f}" .format(r2))