# Exemplo 74 - contagem de palavras

texto = input("Digite um texto: ")
pontuacao = [".",",",":",";","!","?"]

# remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p, " ")

# split devolve a lista com palavras como itens
num_palavras = len(texto.split())
print("Número de palavras:", num_palavras)
