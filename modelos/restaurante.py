class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
print(dir(restaurante_praca)) # 'dir' vai mostrar atributos, listar métodos e propriedades de um objeto
print(vars(restaurante_praca)) # 'vars' vai mostrar em forma de dicionário os atributos da classe
print(restaurante_praca.ativo)