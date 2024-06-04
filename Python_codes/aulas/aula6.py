
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
 
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False


    def devolver(self):
        if not self.disponivel:
            self.disponivel = True


class Biblioteca():
    def __init__(self,):
        self.lista_de_livros =[]

    def adicionar_livro (self,Livro):
        self.lista_de_livros.append((Livro))
        print('ADICIONADO COM SUCESSO')

    def listar_livro(self):
        for cont in range (len(Bibliotecas)):
            print(f'O NOME É: {Bibliotecas[cont]['titulo']} \n , O AUTOR É:  {Bibliotecas[cont]['autor']} \n O ISBN É {Bibliotecas[cont]['isbn']}!')