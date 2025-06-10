# Exemplo 85 - calculadora com a função lambda
soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b

print("Calculadora com a função lambda")
while True:
    print("[1] - Soma\n[2] - Substração\n[3] - Multiplicação\n[4] - Divisão\n[0] - Sair")
    op = int(input("Digite uma opção: "))
    if op == 0:
        print("Obrigado por utilizado o programa !!!")
        break
    elif op < 0 or op > 4:
        print("Opção inválida")
    else:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if op == 1:
            print("%.2f" %(soma(a,b)))
        elif op == 2:
            print("%.2f" %(subtracao(a,b)))
        elif op == 3:
            print("%.2f" %(multiplicacao(a,b)))
        else:
            print("%.2f" %(divisao(a,b)))
