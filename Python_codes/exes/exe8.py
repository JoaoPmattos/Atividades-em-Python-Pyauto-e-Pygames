i=0
while i <=10:
    idade=int (input (' Digite sua idade: '))
    if idade >= 18:
        print (' Voce é maior de idade! ')
        i+=1
    elif idade <0:
        print(' Você é um feto! ')
    else:
        print(' Você é menor de idade! ')
        i+=1
print (' FIM! ')


# for i in range(10):
#     idade = int(input(' Insira sua idade: ')) 
#     if idade >=18:
#         print (' Voce é maior de idade! ')
#     elif idade <0:
#         print('Você é um feto!')
#     else:
#         print(' Voce é menor de idade! ')
# print('Fim!')

