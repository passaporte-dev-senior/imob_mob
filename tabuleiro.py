import random


def dado():
    return random.randint(1, 6)


class Tabuleiro:
    def __init__(self, propriedades, jogadores):
        self.propriedades = propriedades     
        self.jogadores = {}
        for jogador in jogadores:
            self.jogadores[jogador] = 0
            
    def movimenta(self, jogador, passos):
        posicao_atual = self.jogadores[jogador]
        nova_posicao = posicao_atual + passos

        if nova_posicao > 20:
            nova_posicao -= 20
            jogador.saldo += 100 

        self.jogadores[jogador] = nova_posicao

        if self.propriedades:
            propriedade = self.propriedades[nova_posicao]

            jogador.paga(propriedade)

    
    def posicao(self, jogador):
        return self.jogadores[jogador]