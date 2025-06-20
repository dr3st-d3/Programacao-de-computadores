# Criação da Classe
class Pessoa:
    "Isso é uma classe nova chamada Pessoa"
    
    idade = 15  # atributo de classe
    
    def saudacao(self):
        print("Olá Pessoas!")

# Output: 15
print(Pessoa.idade)

# Output: <function Pessoa.saudacao>
print(Pessoa.saudacao)

# Output: "Isso é uma classe nova chamada Pessoa"
print(Pessoa.__doc__)

# Criação do Objeto da classe Pessoa
matheus = Pessoa()

# Output: 15
print(matheus.idade)

# Output: <bound method Pessoa.saudacao of <__main__.Pessoa object>>
print(matheus.saudacao)

# Chamando o método saudacao()
# Output: "Olá Pessoas!"
matheus.saudacao()
