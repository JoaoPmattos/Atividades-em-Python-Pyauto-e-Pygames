def soma(a,b):
    c = a+b
    print (f'O resultado da soma é: {c}')

def subtracao(a,b):
    c= a-b
    print (f'O resultado da subtração é: {c}')

def multiplicacao(a,b):
    c=a*b
    print(f'O resultado da multiplicação é: {c}')

def divisao(a,b):
    if b ==0:
        print('ERRO, não é possivel dividir por zero')
    else:
         print(f'O resultado da sua divisão é: {a/b}')


print('BEM-VINDO A CALCULADORA ;) ')

while True:
    selecao=int(input('\n DIGITE: \n [1] PARA SOMA: \n [2] PARA SUBTRAÇÃO: \n [3] PARA MULTIPLICAÇÃO: \n [4] PARA DIVISÃO: \n [0] PARA SAIR: \n RESPOSTA:' ))
    if selecao ==0:
        break
    valor1=int(input('DIGITE O PRIMEIRO VALOR: '))
    valor2=int(input('DIGITE O SEGUNDO VALOR: '))
   
    if selecao ==1:
        soma (valor1,valor2)
    elif selecao ==2:
        subtracao(valor1,valor2)
    elif selecao ==3:
        multiplicacao(valor1,valor2)
    elif selecao ==4:
        divisao(valor1,valor2)
    else:
        print ('ERRO, selecione outra opção: ')
print('DESLIGANDO...')