class Pessoa:
    def __init__(self, nome, idade=int, profissao=''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá sou o {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá sou o {self.nome}!'

    def aniversario(self):
        self.idade += 1
    
pessoa1 = Pessoa('Fabrizio', 19, 'Engenheiro de Software')
pessoa2 = Pessoa('Bianca', 18, 'Psicóloga')
pessoa3 = Pessoa('Victor', 20)

print('Informações Iniciais:')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print('Informações após o aniversário:')
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)