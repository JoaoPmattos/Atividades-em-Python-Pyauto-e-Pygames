idade = []
nomes = []

for i in range(5):
    idade.append(int(input('Insira sua idade: ')))
    nomes.append(input('Insira o seu nome: '))

procura = int(input('Selecione um indice de [1] a [5] para pesquisar: '))

procura -=1
print(idade[procura])
print(nomes[procura])
