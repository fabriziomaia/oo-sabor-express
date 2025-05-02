class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f'Conta de {self._titular} - Saldo: R${self._saldo},00'

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancariaPythonica('Fabrizio', 2500000)
conta2 = ContaBancariaPythonica('Bianca', 1551200)
conta3 = ContaBancariaPythonica('Victor', 12)
conta4 = ContaBancariaPythonica('Enzo', 50)

print(conta1)
print(conta2)

print(f'Antes de ativar: Conta 3 ativa? {conta3._ativo}')
ContaBancariaPythonica.ativar_conta(conta3)
print(f'Depois de ativar conta: Conta 3 ativa? {conta3._ativo}')

print(f'Titular da conta 4: {conta4.titular}')

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self. endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco('João', 25, 'Rua A', '155.600.566-00', 'Desenvolvedor')
cliente2 = ClienteBanco('Maria', 22, 'Rua B', '185.360.656-10', 'Analista')
cliente3 = ClienteBanco('Chiquinho', 23, 'Rua C', '885.674.952-55', 'Empresário')

conta_cliente1 = ClienteBanco.criar_conta('Joana', 100)
print(f'Conta de {conta_cliente1.titular} criada com saldo inicial de {conta_cliente1.saldo}')