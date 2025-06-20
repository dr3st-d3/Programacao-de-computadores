# Exemplo 40 - 
salario = 0
contagem = 12
for i in range(1, 13):
    if i == 1:
        valor = float(input("Digite seu salário de Janeiro: "))
    elif i == 2:
        valor = float(input("Digite seu salário de Fevereiro: "))
    elif i == 3:
        valor = float(input("Digite seu salário de Março: "))
    elif i == 4:
        valor = float(input("Digite seu salário de Abril: "))
    elif i == 5:
        valor = float(input("Digite seu salário: de Maio: "))
    elif i == 6:
        valor = float(input("Digite seu salário de Junho: "))
    elif i == 7:
        valor = float(input("Digite seu salário de Julho: "))
    elif i == 8:
        valor = float(input("Digite seu salário de Agosto: "))
    elif i == 9:
        valor = float(input("Digite seu salário de Setembro: "))
    elif i == 10:
        valor = float(input("Digite seu salário de Outubro: "))
    elif i == 11:
        valor = float(input("Digite seu salário de Novembro: "))
    elif i == 12:
        valor = float(input("Digite seu salário de Dezembro: "))
    if valor > 0:
        salario += valor
        contagem += 1
media = salario / contagem
ferias = media * 1/3
print("O valor do 13° salário é de R$ %2d" %(media))
print("O valor de férias é de R$ %2d" %(ferias))