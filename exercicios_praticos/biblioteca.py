from pratica7 import Livro

livro_biblioteca = Livro('Fenix', 'Victor Asfur', 2021)
print(f'Antes de emprestar: o livro está disponivel? {livro_biblioteca._disponivel}')
livro_biblioteca.emprestar()
print(f'Depois de emprestar: o livro está disponivel? {livro_biblioteca._disponivel}')

ano_especifico = 1623
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}')