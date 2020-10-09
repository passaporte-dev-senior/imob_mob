# Desafio do Banco Imobiliário

Considere o seguinte jogo hipotético muito semelhante a Banco Imobiliário, onde várias de suas mecânicas foram simplificadas.

Numa __partida__ desse __jogo__, os __jogadores__ se alternam em __rodadas__, numa ordem definida aleatoriamente no começo da partida. Os jogadores sempre começam uma partida com __saldo__ de 300 para cada um.

Nesse jogo, o __tabuleiro__ é composto por 20 __propriedades__ em sequência. Cada propriedade tem um custo de venda, um valor de aluguel, um __proprietário__ caso já estejam compradas, e seguem uma determinada ordem no tabuleiro. 

Não é possível construir hotéis e nenhuma outra melhoria sobre as propriedades do tabuleiro, por simplicidade do problema. 

No começo da sua vez, o jogador joga um __dado equiprovável de 6 faces__ que determina quantos __espaços no tabuleiro__ o jogador vai andar.

Ao cair em uma propriedade sem __proprietário__, o jogador pode escolher entre comprar ou não a propriedade. Esse é a única forma pela qual uma propriedade pode ser comprada.

Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da propriedade.

Ao completar uma volta no tabuleiro, o __jogador__ ganha 100 de __saldo__.

Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda.

Ao comprar uma propriedade, o jogador perde o dinheiro e ganha a posse da propriedade. 

Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente.

Um jogador que fica com __saldo negativo__ perde o jogo, e não joga mais. Perde suas propriedades e portanto podem ser compradas por qualquer outro jogador. 

__Termina__ quando __restar__ somente um jogador com __saldo positivo__, a qualquer momento da partida. Esse jogador é declarado o vencedor.

Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida com 4 diferentes tipos de possíveis jogadores.

Os comportamentos definidos são:
* O __jogador impulsivo__ compra qualquer propriedade sobre a qual ele parar.
* O __jogador exigente__ compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
* O __jogador cauteloso__ compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
* O __jogador aleatório__ compra a propriedade que ele parar em cima com probabilidade de 50%.

Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta partida.
