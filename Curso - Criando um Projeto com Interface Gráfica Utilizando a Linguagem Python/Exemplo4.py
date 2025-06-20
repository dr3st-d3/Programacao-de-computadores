from funcionarios import *

f1 = Funcionario("Matheus", "matheus@email.com")

f1.cadastro_hora("Jan", 300)
f1.cadastro_hora("Fev", 200)
f1.cadastro_salario_hora("Jan", 30)
f1.cadastro_salario_hora("Fev", 30)

print(f1)

print(f1.calcula_salario("Jan"))
print(f1.calcula_salario("Fev"))