from itertools import cycle

from simob import *
from tabuleiro import *

class Partida:

    def __init__(self):

        jogadores = Jogadores(
            Jogador(impulsivo),
            Jogador(exigente),
            Jogador(cauteloso),
            Jogador(aleatorio)
        ).embaralha()

        precos_e_alugueis = ((200, 90),) * 20

        propriedades = [Propriedade(preco, aluguel) for preco, aluguel in precos_e_alugueis]

        tabuleiro = Tabuleiro(propriedades, jogadores)

        os_jogadores = cycle(jogadores)

        global LIMITE_DE_RODADAS
        while LIMITE_DE_RODADAS:
            jogador = next(os_jogadores)
            if jogador:
                tabuleiro.movimenta(jogador, dado())
            if jogadores.resta_um_jogador():
                self.vencedor = jogadores.vencedor()
                print(jogadores.vencedor())
                break
            LIMITE_DE_RODADAS -= 1
        else:
            self.vencedor = jogadores.vencedor()
            print(jogadores.vencedor(), jogadores)


partidas = []
for i in range(1000):
    partidas.append(Partida())

from collections import Counter
from pprint import pprint

pprint(Counter([p.vencedor.estrategia.__name__ for p in partidas]))
