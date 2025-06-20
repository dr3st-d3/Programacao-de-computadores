# Exemplo 37b - comando continue com while
i = 0
while (i <= 10):
    i += 1
    if (i-1) == 5:
        continue
    print("\nO número do laço é %d" %(i-1))
