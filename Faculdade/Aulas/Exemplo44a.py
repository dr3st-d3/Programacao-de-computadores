# Exemplo 44a - calculo de média de um aluno com listas
notas = [6, 7.5, 5.0, 8.5, 9.5]
soma = 0
for i in range(5):
    soma += notas[i]
media = soma / 5
print("A média do aluno é %.2f" %(media))
