# Exemplo 39 - tabuada de 1 a 10 com while
tabuada = 1
while (tabuada <=10):
    print("\n")
    numero = 0
    while (numero <=10):
        print("%2d * %2d = %2d" %(tabuada, numero, tabuada*numero))
        numero += 1
    tabuada += 1
