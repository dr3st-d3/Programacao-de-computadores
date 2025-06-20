# Passagem por valor (imutáveis, como números)
def por_valor(x):
    x += 10
    print(f"Valor dentro da função: {x}")

num = 5
por_valor(num)
print(f"Valor fora da função: {num}")  # O valor original permanece inalterado

# Passagem por referência (mutáveis, como listas)
def por_referencia(lista):
    lista.append(10)
    print(f"Lista dentro da função: {lista}")

valores = [1, 2, 3]
por_referencia(valores)
print(f"Lista fora da função: {valores}")  # A lista original foi modificada
