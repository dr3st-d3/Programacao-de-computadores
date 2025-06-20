# Exemplo 83 - utilização de arquivos externos
import metodos

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

op = int(input("1 - Soma\n2 - Subtração\nDigite uma opção: "))
if op == 1:
    print(metodos.somaValores(a,b))
elif op == 2:
    print(metodos.subtraiValores(a,b))
else:
    print("Opção inválida")

metodos.fim()
