idade =int(input('insira uma idade'))

if idade <0:
    print('idade invalida')
elif idade <18:
    print('menor de idade!')
elif idade <65:
    print('pré adolescente!')
else:
    print('menor de idade!')
print('FIM!')

