total = int(input('Insira a quantidade de pessoas que irão votar! '))
jose = 0
maria = 0
marcia = 0
nulo = 0
i = 1
while i <= total:
    votos=int(input(' Selecione [11] para José, [22] para Maria e [33] para Marcia! '))
    if votos == 11:
        print (' Um voto para José! ')
        jose +=1
    elif votos == 22:
        print (' Um voto para Maria! ')
        maria +=1
    elif votos == 33:
        print (' Um voto para Marcia! ')
        marcia +=1
    else:
        print (' Voto Nulo! ')
        nulo +=1
    i+=1
print(f'O candidato José ficou com {jose} votos! A candidata Maria ficou com {maria} votos! E a candidata Marcia ficou com {marcia} votos! E houveram {nulo} votos nulos! ')
if jose > maria and jose > marcia:
    print ('José Ganhou')
elif maria > marcia and maria > jose:
    print ('Maria Ganhou! ')
elif marcia > maria and marcia > jose:
    print ('Marcia Ganhou! ')
else:
    print ('Empate! ')
print(' FIM! ')
    
    