# Exemplo 81 - exemplo de dois métodos: uma função e um procedimento

def calculoIMC(peso, alt):
    result = peso / altura ** 2
    return(result)

def despedida():
    print("Obrigado por executar este programa")
    print("Até breve !!!")

peso = float(input("Digite o peso da pessoa em kg: "))
altura = float(input("Digite a altura da pessoa em m: "))

print("O IMC é %.2f kg/m²" %(calculoIMC(peso,altura)))
despedida()
