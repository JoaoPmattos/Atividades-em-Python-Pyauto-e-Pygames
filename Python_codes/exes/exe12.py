
dicionario = {
    'titulo':'Era uma vez',
    'autor':'joao',
    'anopubli':'2020',
    'genero':'terror',
    'paginas':'250'
}

print (dicionario)


tituloalt = 0
autoralt = 0
anopublialt =0
generoalt = 0
paginasalt = 0



alterar =int(input('Aperta [1] para alterar um campo e [2] para sair do codigo:  '))
while alterar==1:
    escolha = int(input('SELECIONE: \n [1] PARA ALTERAR TITULO \n [2] PARA AUTOR \n [3] PARA ANO DE PUBLICAÇÃO \n [4] PARA GENERO \n [5] PARA PAGINAS: \n [6] PARA LISTAR O LIVRO: \n APERTE [0] PARA SAIR: \n '))
    if escolha ==1:
        tituloalt = (input('DIGITE O TITULO DO LIVRO: '))
        dicionario['titulo']= tituloalt
        print ('TITULO ATUALIZADO COM SUCESSO:')
        print (dicionario.items())
    if escolha ==2:
        autoralt = (input('DIGITE O NOME DO AUTOR: '))
        dicionario ['autor'] = autoralt
        print ('AUTOR ATUALIZADO COM SUCESSO:')
        print (dicionario.items())
    if escolha ==3:
        anopublialt = int(input('DIGITE O O ANO DE PUBLICAÇÃO: '))
        dicionario ['anopubli'] = anopublialt
        print ('ANO ATUALIZADO COM SUCESSO! ')
        print (dicionario.items())
    if escolha == 4:
        generoalt = (input('DIGITE O GENERO DO LIVRO: '))
        dicionario ['genero'] = generoalt
        print ('GENERO ATUALIZADO COM SUCESSO! ')
        print (dicionario.items())
    if escolha ==5:
        paginasalt = int(input('DIGITE O NUMERO DE PAGINAS: '))
        dicionario ['paginas'] = paginasalt
        print ('PAGINAS ATUALIZADAS COM SUCESSO!')
        print (dicionario.items())
    if escolha ==6:
        print('EXIBINDO DICIONARIO: ')
        print (dicionario.items())
    if escolha ==0:
        print ('FIM DO CODIGO')
        print (dicionario.items())
        break
print ('CODIGO ENCERRADO! ')

        

#     for i in range (5):
#         tituloalt = input('insira o nome do livro: ')
#         autoralt = input('insira o autor: ')
#         anopublialt = int(input('insira o ano de publicação: '))
#         generoalt= input('insira o genero do livro: ')
#         paginasalt = int(input('insira a quantidades de paginas do livro: '))
#         dicionario ={
#             'titulo': tituloalt,
#             'autor':autoralt,
#             'anopubli': anopublialt,
#             'genero':generoalt,
#             'paginas':paginasalt
#     }
#         print (dicionario.items())
# else:
#     print('FIM DO CODIGO! ')

