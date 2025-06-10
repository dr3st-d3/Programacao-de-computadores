# Exemplo 21 - 
diaria = int(input("Digite a quantidade de diárias: "))
tipo = input("Digite o tipo de diária: ")

if tipo == 's' or tipo == 'S':
    print("\nO valor total a ser pago é R$ %.2f" %(diaria * 255.5))
elif tipo == 'd' or tipo == 'D':
    print("\nO valor total a ser pago é R$ %.2f" %(diaria * 305.5))
elif tipo == 't' or tipo == 'T':
    print("\nO valor total a ser pago é R$ %.2f" %(diaria * 360.5))
    
else:
    print("\nTipo de diária inválida.")
