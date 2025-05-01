# Ex1.
class Carro:

    def __init__(self, modelo, cor, ano=int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Creta', 'Branco', 2019)
print(vars(carro1))

# Ex2.
class Restaurante:

    def __init__(self, nome, categoria, avaliacao, preco):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao = avaliacao
        self.preco = preco
        self.ativo = False

restaurante1 = Restaurante('Pizza Hut', 'Italiana', '5', 'Médio')
print(vars(restaurante1))

# Ex3.
class Restaurante:

    def __init__(self, nome, categoria, avaliacao, preco, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao = avaliacao
        self.preco = preco
        self.ativo = ativo

restaurante1 = Restaurante('Pizza Hut', 'Italiana', '5', 'Médio')
print(vars(restaurante1))

# Ex4.
class Restaurante:

    def __init__(self, nome, categoria, avaliacao, preco, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao = avaliacao
        self.preco = preco
        self.ativo = ativo
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante1 = Restaurante('Pizza Hut', 'Italiana', '5', 'Médio')
print(restaurante1)

# Ex5.
class Cliente:

    def __init__(self, nome, idade, cor, sexo):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo

cliente1 = Cliente('Fabrizio', 19, 'Branco', 'Masculino')
cliente2 = Cliente('Bianca', 18, 'Branco', 'Feminino')
cliente3 = Cliente('Will Smith', 56, 'Preta', 'Masculino')

print(vars(cliente1))
print(vars(cliente2))
print(vars(cliente3))