from simob import *
from tabuleiro import *

jogadores = Jogadores(
    Jogador(impulsivo),
    Jogador(exigente),
    Jogador(cauteloso),
    Jogador(aleatorio)
)#.embaralha()

jogadores.limite_de_rodadas = 50

precos_e_alugueis = ((30, 3),) * 10

propriedades = [Propriedade(preco, aluguel) for preco, aluguel in precos_e_alugueis]
print(propriedades)

tabuleiro = Tabuleiro(propriedades, jogadores.jogando)

for jogador in jogadores:
    print(jogadores.rodadas, end='')
    tabuleiro.movimenta(jogador, dado())
    # jogador.movimenta(tabuleiro, dado())
    # jogador.joga(tanbuleiro)
else:
    print(jogadores.vencedor())