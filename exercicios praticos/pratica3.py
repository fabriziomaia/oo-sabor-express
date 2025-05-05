class Musica:

    def __init__(self, nome, artista, duracao=int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
musica1 = Musica('Mil Maneiras', 'Veigh', 131)
musica2 = Musica('Se eu atendo o telefone', 'GA', 182)
musica3 = Musica('BAD!', 'XXXTentacion', 96)
print(vars(musica1))
print(vars(musica2))
print(vars(musica3))
