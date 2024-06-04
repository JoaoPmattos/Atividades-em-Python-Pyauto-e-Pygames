
def mediaa (media):
    soma = 0
    for cont in range (len(media)):
        soma = soma + media[cont]
    return soma/ len(media)
   
def maiorValor (media):
    if len(media) == 0:
        return None
    maiorV = media[0]
    for cont in range (1,len(media)):
        if media[cont]>maiorV:
            maiorV = media[cont]
        return maiorV
    
def menorValor (media):
        if len(media) == 0:
            return None
        menorN = media[0]
        for cont in range (1,len(media)):
            if media[cont] < menorN:
                menorN = media[cont]
        return menorN

media = []
while True:
    media.append(int(input('INSIRA SUA NOTA: ')))
    selecao = int(input('PRESSIONE [1] PARA CONTINUAR E [2] PARA SAIR: '))
    if selecao ==2:
        print('DESLIGANDO')
        break


print ('O resultado da sua media é:', mediaa(media))
print ('Sua menor nota foi:', menorValor(media))
print ('Sua maior nota foi:', maiorValor(media))





# notas=[]
# def media(notas):
#     for i in range(len(notas)):
#         media=notas[i]/len(notas)
#         print (f'A média é de {media}')
   
# def maior(notas):
#     numeromaior=0
#     for i in range(len(notas)):
#         if notas[i]>numeromaior:
#             numeromaior=notas[i]
#             return numeromaior
# def menor(notas):
#     numeromenor=0
#     for i in range(len(notas)):
#         if notas[i]<numeromenor:
#             numeromenor=notas[i]
#             return numeromenor
 
# while True:
#     nota = int(input('Digite uma nota para o seu vetor: '))
#     notas.append(nota)
#     escolha = input('Quer continuar? S/N ')
#     if escolha.upper() == 'N':
#         break
 
# media(notas)
# print(f'A maior nota é: {maior(notas)}')
# print(f'A menor nota é: {menor(notas)}')
 
