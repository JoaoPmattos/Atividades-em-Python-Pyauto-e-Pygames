nota1=float(input('Insira a sua primeira nota!'))
nota2=float(input('Insira sua segunda nota!'))
nota3=float(input('Insira sua terceira nota!'))
soma= nota1+nota2+nota3
media = soma/3
print(f'A soma de todas as notas resultou em {soma} e sua media resultou em: {media} pontos')

if media>=7:
    print(f'média{media}, aluno APROVADO!')
elif media <=3:
    print(f'média{media}, aluno REPROVADO!')
else:
    print(f'média{media}, aluno RECUPERAÇÃO!')
