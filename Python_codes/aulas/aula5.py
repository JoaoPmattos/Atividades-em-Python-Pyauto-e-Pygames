class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def mostrar_informacoes(self):
        print (f'AQUI ESTÃO SUAS INFORMAÇÕES: \n MARCA: {self.marca} \n MODELO: {self.modelo} \n ANO: {self.ano} ')

carro = Veiculo (input('QUAL O NOME DO CARRO? '),(input('QUAL O MODELO DO CARRO? ')),int(input('QUAL O ANO DO CARRO? ')))
print('-'*30)
moto = Veiculo (input('QUAL O NOME DA MOTO? '),(input('QUAL O MODELO DA MOTO? ')),int(input('QUAL O ANO DA MOTO? ')))
print('-'*30)
navio = Veiculo(input('QUAL O NOME DO NAVIO? '),(input('QUAL O MODELO DO NAVIO? ')),int(input('QUAL O ANO DO NAVIO? ')))

carro.mostrar_informacoes()
print('-'*30)
moto.mostrar_informacoes()
print('-'*30)
navio.mostrar_informacoes()
print('-'*30)