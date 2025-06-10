# Exemplo 40b - cálculo do 13º salário e 1/3 de férias com estrutura de repetição e listas
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
salario = 0
contagem = 0
for i in range(12):
    valor = float(input("Digite o salário do mês de %s em R$ " %(mes[i])))
    if valor > 0:
        salario += valor
        contagem += 1
media = salario / contagem
ferias = media * 1/3
print("O valor do 13º salário é R$ %.2f" %(media))
print("O valor de férias é R$ %.2f" %(ferias))
