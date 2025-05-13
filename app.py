from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
# restaurante_praca.receber_avaliacao('Gui', 5)
# restaurante_praca.receber_avaliacao('Lais', 4)
# restaurante_praca.receber_avaliacao('Emy', 2)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

def main():
    # Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()