import random
from simob import Jogador, Propriedade, impulsivo
from tabuleiro import Tabuleiro, dado

def lista_propriedades():
    return [Propriedade(preco=0, aluguel=0)] * 20
    
def test_move_jogador_um_passo():    
    jogador = Jogador(impulsivo)
    tabuleiro = Tabuleiro(propriedades=lista_propriedades(), jogadores=[jogador])
    assert tabuleiro.posicao(jogador) == 0
    tabuleiro.movimenta(jogador, passos=1)
    assert tabuleiro.posicao(jogador) == 1

def test_move_jogador_dois_passos():
    jogador = Jogador(impulsivo)
    tabuleiro = Tabuleiro(propriedades=lista_propriedades(), jogadores=[jogador])
    assert tabuleiro.posicao(jogador) == 0
    tabuleiro.movimenta(jogador, passos=2)
    assert tabuleiro.posicao(jogador) == 2

def test_inicializa_dois_jogadores():
    jogador_1 = Jogador(impulsivo)
    jogador_2 = Jogador(impulsivo)
    lista_jogadores = [jogador_1, jogador_2]
    tabuleiro = Tabuleiro(propriedades=lista_propriedades(), jogadores=lista_jogadores)
    assert tabuleiro.posicao(jogador_1) == 0
    assert tabuleiro.posicao(jogador_2) == 0

def test_se_jogador_volta_ao_inicio():
    jogador = Jogador(impulsivo)
    tabuleiro = Tabuleiro(propriedades=lista_propriedades(), jogadores=[jogador])
    assert tabuleiro.posicao(jogador) == 0
    tabuleiro.movimenta(jogador, passos=25)
    assert tabuleiro.posicao(jogador) == 5
    assert jogador.saldo == 400
    
def test_move_jogador_um_passo_com_dado():
    jogador = Jogador(impulsivo)
    tabuleiro = Tabuleiro(propriedades=lista_propriedades(), jogadores=[jogador])
    assert tabuleiro.posicao(jogador) == 0
    random.seed(2)
    passo = dado()
    tabuleiro.movimenta(jogador, passos=passo)
    assert tabuleiro.posicao(jogador) == 1
    tabuleiro.movimenta(jogador, passos=dado())
    assert tabuleiro.posicao(jogador) == 2
    random.seed()

def test_move_jogador_um_passo_com_propriedade():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(preco=100)

    tabuleiro = Tabuleiro(propriedades=[propriedade], jogadores=[jogador])

    assert tabuleiro.posicao(jogador) == 0
    tabuleiro.movimenta(jogador, passos=1)
    assert tabuleiro.posicao(jogador) == 1

    assert jogador.saldo == 200
    assert propriedade.proprietario == jogador