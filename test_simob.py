from simob import *

def test_comprar_com_proprietario():
    jogador = Jogador(exigente)
    proprietario = Jogador(exigente)
    propriedade = Propriedade(100, 51)
    propriedade.proprietario = proprietario

    jogador.paga(propriedade)

    assert jogador.saldo == 249
    assert proprietario.saldo == 351

def test_exigente_sem_saldo():
    jogador = Jogador(exigente)
    propriedade = Propriedade(400, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 300

def test_exigente_com_saldo_mas_aluguel_inferior_a_50():
    jogador = Jogador(exigente)
    propriedade = Propriedade(100, 40)
    jogador.paga(propriedade)
    assert jogador.saldo == 300


def test_exigente_com_saldo():
    jogador = Jogador(exigente)
    propriedade = Propriedade(100, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 200

def test_aleatorio_sem_saldo_true():
    random.seed(42)

    jogador = Jogador(aleatorio)
    propriedade = Propriedade(400, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 300
    random.seed()

def test_aleatorio_com_saldo_false():
    random.seed(0)

    jogador = Jogador(aleatorio)
    propriedade = Propriedade(100, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 300
    random.seed()

def test_aleatorio_com_saldo_true():
    random.seed(42)

    jogador = Jogador(aleatorio)
    propriedade = Propriedade(100, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 200
    random.seed()

def test_cauteloso_com_saldo_restante_igual_a_80():
    jogador = Jogador(cauteloso)
    propriedade = Propriedade(220, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 80

def test_cauteloso_com_saldo_restante_maior_que_80():
    jogador = Jogador(cauteloso)
    propriedade = Propriedade(210, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 90

def test_cauteloso_com_saldo_restante_menor_que_80():
    jogador = Jogador(cauteloso)
    propriedade = Propriedade(230, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 300

def test_impulsivo_com_saldo():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(150, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 150

def test_impulsivo_com_saldo_igual_preco():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(300, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 0

def test_impulsivo_sem_saldo():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(301, 51)
    jogador.paga(propriedade)
    assert jogador.saldo == 300
