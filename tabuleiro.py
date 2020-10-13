import random


def dado():
    return random.randint(1, 6)


class Tabuleiro:
    def __init__(self, propriedades, jogadores):        
        self.jogadores = {}
        for jogador in jogadores:
            self.jogadores[jogador] = 0
            
    def movimenta(self, jogador, passos):
        posicao_atual = self.jogadores[jogador]
        nova_posicao = posicao_atual + passos
        if nova_posicao > 20:
            nova_posicao -= 20
        self.jogadores[jogador] = nova_posicao
    
    def posicao(self, jogador):
        return self.jogadores[jogador]