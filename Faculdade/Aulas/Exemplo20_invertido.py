# Exemplo 20  - resultado final - if-else aninhada
media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite o percentual de freqência do aluno: "))
if frequencia >= 75:
    if media < 6:
        print("\nAluno reprovado por nota.")
    else:
        print("\nAluno aprovado.")
else:
    print("\nAluno reprovado por falta.")