class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'

# Ex1.
restaurante_praca.categoria = 'Italiana'

# Ex2.
nome_do_restaurante = restaurante_praca.nome

# Ex3.
if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# Ex4.
categoria = Restaurante.categoria

# Ex5.
restaurante_praca.nome = 'Bistrô'    

# Ex6.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Ex7.
if restaurante_pizza == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food')

# Ex8.
restaurante_pizza.ativo = True

# Ex9.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
