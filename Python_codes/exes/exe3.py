nome=input('Digite o nome do vendedor!')
salario= float(input('Insira o salario do vendedor!'))
totalVen = float (input('Insira o total de vendas do vendedor!'))
comissao = totalVen * 0.15
salarioTotal= salario + comissao

print(f'O nome do vendedor é: {nome}\n seu salario fixo é de: {salario}\n Por conta de suas vendas, o vendedor conquistou o salario de: {salarioTotal} ')