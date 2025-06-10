# Exemplo 61 - strings com laços de repetição

texto = input("Digite um texto: ")
inverso = " "
for st in texto:
    inverso = st + inverso
    print(st)
print(inverso)
