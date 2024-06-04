# FUNÇÕES
# DECLARAÇÃO DE FUNÇÕES SIMPLES
def mensagem():
    print ('ola mundo!')
    print ('Meu nome é João')

mensagem()
print ('-'*30)
# DECLARAÇÃO DE FUNÇÕES COM PARAMETROS
def hello(meu_nome):
    print(f'Olá {meu_nome}, seja bem vindo!')

hello ('João')

# DECLARAÇÃO DE FUNÇÕES COM PARAMETROS:
def mult (a,b):
    print (f'Resultado da operação é: {a*b}')
    
mult (10,2)
print('-' *30)

# FUNÇÕES COM PARAMETROS E RETORNO:
# def soma(a,b):
#     return a+b

# valor1=int(input('DIGITE O PRIMEIRO VALOR: '))
# valor2=int(input('DIGITE O SEGUNDO VALOR: '))
# print(f'A soma dos valores é: {soma(valor1,valor2)}')

# DECLARAÇÕES DE FUNÇÕES ANÔNIMAS
soma =lambda a,b:a+b

valor1=int(input('DIGITE O PRIMEIRO VALOR: '))
valor2=int(input('DIGITE O SEGUNDO VALOR: '))
print(f'A soma dos valores é: {soma(valor1,valor2)}')

