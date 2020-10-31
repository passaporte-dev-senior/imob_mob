import random

BONUS = 100

def dado():
    return random.randint(1, 6)


class Tabuleiro:
    def __init__(self, propriedades, jogadores):
        self.propriedades = [None] + propriedades     
        self.jogadores = {}
        for jogador in jogadores:
            self.jogadores[jogador] = 0
            
    def movimenta(self, jogador, passos):
        posicao_atual = self.jogadores[jogador]
        nova_posicao = posicao_atual + passos

        if nova_posicao > 20:
            nova_posicao -= 20
            jogador.recebe(BONUS) 

        self.jogadores[jogador] = nova_posicao

        propriedade = self.propriedades[nova_posicao]

        jogador.compra_ou_aluga(propriedade)

    def posicao(self, jogador):
        return self.jogadores[jogador]