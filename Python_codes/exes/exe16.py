lista = []

def novoProduto ():
    nomeProduto = input('INSIRA O NOME DO PRODUTO: ')
    precoUni = int(input('INSIRA O PREÇO UNITARIO DO PRODUTO: '))
    quantiEst = int(input('INSIRA A QUANTIDADE NO ESTOQUE: '))

    listas={
        'nomeProduto':nomeProduto,
        'precoUni':precoUni,
        'quantiEst':quantiEst
    }
    lista.append(listas)\
    
def vender():
    if len(lista)==0:
        print ('NÃO HÁ NADA NO ESTOQUE')
    else:
        nomeProdutoVenda = input('INSIRA O NOME DO PRODUTO QUE DESEJA VENDER: ')
        quantVenda = int(input('INSIRA A QUANTIDADE QUE DESEJA VENDER: '))
        for cont in range (len(lista)):
            if lista[cont]['nomeProduto'] == nomeProdutoVenda:
                lista[cont]['quantiEst'] -= quantVenda
            else:
                print('ERRO,PRODUTO NÃO ENCONTRADO!')
            if lista[cont]['quantiEst'] < quantVenda:
                print('ERRO, NÃO É POSSIVEL VENDER ESSA QUANTIDADE!')

def valorTotal():
    valorTotal = 0
    for cont in range (len(lista)):
        valorTotal += lista[cont]['precoUni'] * lista[cont]['quantiEst']
    print(f'O VALOR DO ESTOQUE É DE: {valorTotal}')

def exibirLista():
   for cont in range (len(lista)):
      print(f'O NOME É: {lista[cont]['nomeProduto']}, O PREÇO É R$: {lista[cont]['precoUni']} E A QUANTIDADE É DE: {lista[cont]['quantiEst']}!')


while True:
    print ('-'*60)
    menu = int(input('\n SELECIONE [1] PARA ADICIONAR NOVOS PRODUTOS: \n SELECIONE [2] PARA VENDER PRODUTOS: \n SELECIONE [3] PARA EXIBIR O VALOR TOTAL DO DO ESTOQUE: \n SELECIONE [4] PARA EXIBIR A LISTA DE PRODUTOS: \n SELECIONE [5] PARA FINALIZAR O SISTEMA: \n INSIRA SUA RESPOSTA:'))
    if menu == 1:
       novoProduto()
    elif menu ==2:
       vender()
    elif menu ==3:
       valorTotal()
    elif menu ==4:
       exibirLista()
    elif menu ==5:
       print('SISTEMA FINALIZANDO... ')
       break
    else:
        print('ERRO! SELECIONE OUTRA OPÇÃO: ')
       
