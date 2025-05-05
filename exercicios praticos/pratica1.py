class Musica:
    nome = ''
    cantor = ''
    ano_lancamento = int

musica1 = Musica()
musica1.nome = 'Mil Maneiras'
musica1.cantor = 'Veigh'
musica1.ano_lancamento = 2022

musica2 = Musica()
musica2.nome = 'Se eu atendo o telefone'
musica2.cantor = 'GA'
musica2.ano_lancamento = 2025

musica3 = Musica()
musica3.nome = 'BAD!'
musica3.cantor = 'XXXTentacion'
musica3.ano_lancamento = 2018


# lista_musica = [nome, cantor, ano_lancamento]

print(vars(musica1))