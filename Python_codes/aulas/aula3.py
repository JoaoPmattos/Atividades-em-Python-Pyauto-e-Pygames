# # DECLARAÇÃO DE LISTA

# nomes = ['sandro','karla','sandro','alice']

# # IMPRIMIR VALORES
# print (nomes)
# #IMPRIMIR VALORES POR INDICE
# print(nomes[0])
# print(nomes[1])
# print(nomes[2])
# print(nomes[3])

# # IMPRIMIR VALORES ENTRE INDICES
# print(nomes[0:2])
# # IMPRIMIR VALORES DE UM INDICE ATE O FINAL
# print(nomes[2:])
# # len () - RETORNA O TAMANHO DA LINHA
# print(len(nomes))

# # LISTAS METODOS
# # ENCONTRA A POSIÇÃO DE UM VALOR ESPECIFICADO
# print(nomes.index('karla'))

# # CONTA QUANTAS VEZES ESSE VALOR SE REPETE
# print(nomes.count('sandro'))

# # ADICIONA UM NOVO ELEMENTO NO FINAL MANUALMENTE
# nomes.append('Joao')
# print(nomes)

# # ADICIONA UM NOVO ELEMENTO NO FINAL DIGITADO PELO USUARIO
# nomes.apprend(input('Digite outro nome! '))
# print (nomes)



# # IMPRIMIR VALORES POR FOR
# for i in range(len(nomes)):
#     print(nomes[i])

# # DECLARAÇÃO E PREENCHIMENTO DA LISTA
# numero = []
# for i in range (10):
#     numero.append(input('Digite um numero! '))
# print (numero)

# # TUPLAS
# # DECLARAÇÃO DE TUPLA
# nome = ('senac','senai','sesi','sesc')

# # IMPRIMIR VALORES
# print(nome)

# # IMPRIMIR VALORES DA TUPLA POR INDICE
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])

# DECLARAÇÃO DE UM DICIONARIO
pessoa={
    'nome':'sandro',
    'idade':18,
    'altura':1.75,
    'aluno':True
}
# IMRPIMIR VALORES
print(pessoa)

# IMPRIMIR VALORES POR INDICE
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['aluno'])

# IMPRIMIR VALORES POR CHAVE
print(pessoa.keys())

# IMPRIMIR VALORES POR VALOR
print(pessoa.values())

# IMPRIMIR VALORES POR ITEM
print(pessoa.items())
0
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')


escola =[]

nomes =input('digite seu nome:')
idades = int(input('digite sua idade:'))
alturas = float(input('digite sua altura'))
pessoa={
    'nome':nomes,
    'idade':idades,
    'altura':alturas
}
escola.append(pessoa)
print(pessoa.items())


# REORDENAR EM ORDEM CRESCENDO GERANDO NOVA LISTA
novo_valor = sorted(valor)
novo_valor =sorted(valor,reverse=True) #DECRESCENTE

# REORDERNAR EM ORDEM CRESCENTE ORIGINAL
valor.sort()
valor.sort(reversed=True) #DECRESCENTE

print(novo_valor)
print(valor)


