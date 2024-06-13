# Como aprendemos na introdução a esse desafio, o vencedor do jogo será determinado por três regras simples:

# Rock vencer a tesoura.
# Scissors vencer o papel.
# Paper vencer a pedra.

# O que você deve considerar nas interações do jogo
# Vamos adicionar um pouco mais de emoção a esse desafio e tornar o jogo multijogador, em que o computador será seu oponente e poderá escolher aleatoriamente um dos elementos (rock, paper ou scissors) para cada movimento, assim como você. Sua interação no jogo será através do console (Terminal).

# O player pode escolher uma das três opções rock, paper ou scissors e deverá ser avisado se inserir uma opção inválida.
# Em cada rodada, o jogador precisa inserir uma das opções na lista e ser informado se venceu, perdeu ou empatou com o adversário.
# Ao final de cada rodada, o player pode escolher se quer jogar novamente.
# Exiba a pontuação do player no final do jogo.
# O minigame precisa lidar com as inserções do usuário, colocando-as em letras minúsculas e informando ao usuário se a opção é inválida.

# Exemplo de interação
# Você escolheu: rock
# O computador escolheu: scissors
# Você venceu!

# Deseja jogar novamente? (yes/no): yes
# Você escolheu: rock
# O computador escolheu: rock
# Empate!

# Deseja jogar novamente? (yes/no): yes
# Você escolheu: rock
# O computador escolheu: paper
# Você perdeu!

# Deseja jogar novamente? (yes/no): no
# Pontuação final: 1

# Dicas
# Use a função input() para receber a entrada do usuário.
# Use a função random.choice() para escolher aleatoriamente um elemento da lista.
# Use a função print() para exibir mensagens ao usuário.
# Use a estrutura de repetição while para manter o jogo em execução enquanto o jogador deseja continuar jogando.
# Use a estrutura de repetição for para iterar sobre a lista de opções válidas.
# Use a estrutura de decisão if/elif/else para determinar o vencedor de cada rodada.
# Use a estrutura de decisão if para verificar se o jogador deseja continuar jogando.
# Use a variável para armazenar a pontuação do jogador.

import random

# Opções válidas
opcoes = ['rock', 'paper', 'scissors']

# Pontuação inicial do jogador e do computador
pontuacao_jogador = 0
pontuacao_computador = 0

# Loop do jogo
while True:
    # Escolha do jogador
    jogador = input("Escolha uma das opções (rock, paper, scissors): ").lower()
    
    # Verificar se a escolha do jogador é válida
    if jogador not in opcoes:
        print("Opção inválida. Tente novamente.")
        continue

    # Escolha do computador
    computador = random.choice(opcoes)
    
    # Determinar o vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == 'rock' and computador == 'scissors') or (jogador == 'scissors' and computador == 'paper') or (jogador == 'paper' and computador == 'rock'):
        print("Você venceu!")
        pontuacao_jogador += 1
    else:
        print("Você perdeu!")
        pontuacao_computador += 1

    # Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (yes/no): ").lower()
    if jogar_novamente != 'yes':
        break

# Exibir a pontuação final
print("Pontuação final: Jogador -", pontuacao_jogador, ", Computador -", pontuacao_computador)