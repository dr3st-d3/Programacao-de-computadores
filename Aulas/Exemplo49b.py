# Exemplo 49b - atribuição e visualização de valores com método append com listas e estrutura de repetição
nomes = []
print("O tamanho inicial da lista 'nomes' é %d" %(len(nomes)))
print("\n")
for i in range(5):
    ref = str(input("Digite um nome: "))
    nomes.append(ref)
print("\n")
print(nomes)
print("\n")
for i in range(5):
    print(nomes[i])
