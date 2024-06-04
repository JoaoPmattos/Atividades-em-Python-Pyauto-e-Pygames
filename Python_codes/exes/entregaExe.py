listaTarefa = []

def novaTarefa():
    nomeTarefa = input('INSIRA O NOME DA TAREFA: ')
    descricao = input('DESCREVA O QUE DESEJA REALIZAR EM SUA TAREFA: ')

    tarefa={
        'nome':nomeTarefa,
        'descricao':descricao,
        'estatus':False
    }
    listaTarefa.append(tarefa)

def exibirTarefa():
    for cont in range(len(listaTarefa)):
        if len(listaTarefa) ==0:
            print ('VOCÊ NÃO POSSUI NENHUMA TAREFA!')
        if listaTarefa[cont]['estatus'] == False:    
            print (f'\n SUA TAREFA É: {listaTarefa[cont]['nome']} \n O NUMERO DE SUA TAREFA É: {[cont+1]} \n A DESCRIÇÃO DA TAREFA É: {listaTarefa[cont]['descricao']} \n SEU STATUS É DE NÃO CONCLUIDA!')
        else:
         print (f'\n SUA TAREFA É: {listaTarefa[cont]['nome']}\n O NUMERO DE SUA TAREFA É: {[cont+1]} \n A DESCRIÇÃO DA TAREFA É: {listaTarefa[cont]['descricao']} \n SEU STATUS É DE CONCLUIDA!')

def marcarConclusao():
    if len(listaTarefa)==0:
        print('VOCÊ NÃO POSSUI TAREFAS!')
    else:
        numeroDaTarefa = int(input('QUAL O NUMERO DA TAREFA QUE DESEJA CONCLUIR?'))
        numeroDaTarefa -=1
        if numeroDaTarefa >=0 and numeroDaTarefa<=len(listaTarefa) :
            print('\n TAREFA FINALIZADA COM SUCESSO!')
            listaTarefa[numeroDaTarefa]['estatus'] =True
        else:
            print('TAREFA NÃO EXISTENTE')


def exibirTarefasPendentes():
    contador =0
    if len(listaTarefa) == 0:
        print('NENHUMA TAREFA PENDENTE!')
    for cont in range(len(listaTarefa)):
        if listaTarefa[cont]['estatus'] == False:
            contador +=1
            print (f' A TAREFA DE NOME: {listaTarefa[cont]['nome']} ESTÁ PENDENTE!')
    print (f'O TOTAL DE TAREFAS PENDENTES {contador}')
    

       

   

while True:
    menu = int(input('\n SELECIONE [1] PARA ADICIONAR UMA NOVA TAREFA: \n SELECIONE [2] PARA EXIBIR A LISTA DE TAREFAS: \n SELECIONE [3] PARA MARCAR UMA TAREFA COMO CONCLUIDA: \n SELECIONE [4] PARA EXIBIR NÚMERO DE TAREFAS PENDENTES: \n SELECIONE [5] PARA SAIR DO SISTEMA: \n INSIRA SUA RESPOSTA: '))
    if menu ==1:
        novaTarefa()
    elif menu ==2:
        exibirTarefa()
    elif menu ==3:
        marcarConclusao()
    elif menu ==4:
        exibirTarefasPendentes()
    elif menu ==5:
       print('SISTEMA FINALIZANDO...')
       break
    else:
        print('ERRO, TENTE NOVAMENTE! ')
