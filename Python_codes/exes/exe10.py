valor = 0
maior = 0 
soma = 0
menor = 0
media = 0
quanti = 0


while valor >= 0:
    valor = int(input(' Insira um valor: '))

    if valor <0:
        break
    if menor == 0:
        menor = valor
    elif valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor
    else:
        menor = menor
    soma += valor
    quanti +=1
media = soma/quanti
print ('-'*60)
print (f' O maior valor inserido foi: {maior} \n O menor valor inserido foi: {menor}\n A soma de todos os numeros foi: {soma}\n A media foi de: {media} ')
print ('-'*60)

    