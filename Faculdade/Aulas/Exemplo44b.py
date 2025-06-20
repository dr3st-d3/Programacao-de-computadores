# Exemplo 44b - cálculo de média de um aluno com listas
notas = [6, 7.5, 5.0, 8.5, 9.5]
soma = 0
for i in notas:
    soma += i
media = soma / 5
print("A média do aluno é %.2f" %(media))
