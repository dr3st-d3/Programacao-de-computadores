# Exemplo 44c - cálculo de média de um aluno com listas
notas = [6, 7.5, 5.0, 8.5, 9.5, 5.7, 3.0]
soma = 0
for i in range(len(notas)):
    soma += notas[i]
media = soma / len(notas)
print("A média do aluno é %.2f" %(media))
