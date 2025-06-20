# Exemplo 38 - tabuada de 1 a 10 com for
for i in range(1, 11):
    print("\n")
    for j in range(11):
        print("%2d * %2d = %2d" %(i, j, i*j))
