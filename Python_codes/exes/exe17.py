#PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
#PRIMEIRA FORMA
class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
 
    def mudar_nome(self):
        self.nome = input("Qual o seu nome ")
        print(f'Olá {self.nome} seja bem vindo')
 
    def mudar_idade(self):
        self.idade = int(input("Qual sua idade "))
 
    def mudar_cpf(self):
        self.cpf = int(input("Qual o seu CPF "))
       
nomePessoa = input("Digite seu nome ")
idadePessoa = int(input("Digite sua idade "))
cpfPessoa = int(input("Digite seu CPF "))
 
eu = Pessoa(nomePessoa,idadePessoa,cpfPessoa)
 
# #SEGUNDA FORMA
# voce=Pessoa (input("Qual o seu nome: "), int(input("Qual a sua idade ")), int(input("Qual o seu CPF ")))
 
 
# #Terceira forma
# nos=Pessoa('Lucas',20,123456789)
 
#PRINTANDO
print(f'O nome é: {eu.nome}')
print(f'A idade é: {eu.idade}')
print(f'O CPF é: {eu.cpf}')
 
# print(f'O nome é: {voce.nome}')
# print(f'A idade é: {voce.idade}')
 
# #CHAMANDO OS METODOS
# eu.mudar_nome()
# print(f'o nome alterado é {eu.nome}')
# eu.mudar_idade()
# print(f'a idade alterada é {eu.idade}')
# eu.mudar_cpf()
# print(f'o cpf alterado é {eu.cpf}')
 
 
 
class Aluno (Pessoa):
    def __init__(self, nome, idade, cpf,matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cpf: {self.cpf}')
        print(f'Matricula: {self.matricula}')
       
 
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, cargo):
        super().__init__(nome, idade, cpf)
        self.cargo = cargo
        self.salario = 0
 
    def definir_salario(self):
        self.salario = int(input("Digite seu salario"))
 
    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cpf: {self.cpf}')
        print(f'Cargo: {self.cargo}')
 
#Uso de herança
aluno1 = Aluno ('Ana',20,123456789,'2022001')
aluno1.exibir_informacoes()
aluno1.mudar_idade()
 
funcionario1 = Funcionario('José',30,987654321,'Analista')
funcionario1.exibir_informacoes()
funcionario1.mudar_nome()

