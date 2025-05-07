class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Livro: {self._titulo} - autor: {self._autor} - ano de lançamento: {self._ano_publicacao}'

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return [str(livro) for livro in livros_disponiveis]
    
livro1 = Livro('Dom Quixote', 'Miguel de Cervantes', 1605)
livro2 = Livro('Hamlet', 'William Shakespeare', 1623)

print(livro1)
print(livro2)

livro3 = Livro("trallala", 'Joao', 2023)
print(f'Antes de emprestar: o livro está disponível? {livro3._disponivel}')
livro3.emprestar()
print(f'Depois de emprestar: o livro está disponível? {livro3._disponivel}')

Livro.livros = [livro1, livro2, livro3]