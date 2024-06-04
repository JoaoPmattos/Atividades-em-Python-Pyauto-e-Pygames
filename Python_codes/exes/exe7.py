numero = int(input('insira o primeiro valor!'))
numero2=int(input('insira o segundo valor!'))

if numero == numero2:
    print ('numeros são iguais!')
elif numero > numero2:
    print (f'Os numeros são diferentes, {numero} maior que {numero2}!')
else:
    print (f'Os numeros são diferentes, {numero2} maior que {numero}!')
print('fim!')
