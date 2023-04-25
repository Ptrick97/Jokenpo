import random


def opcoes_jokenpo():
    return ['Pedra', 'Papel', 'Tesoura']


def escolher_jogada_do_usuario():
    while True:
        jogada= str(input('Escolha sua jogada (Pedra, Papel ou Tesoura): ')).title()
        if jogada in opcoes_jokenpo():
            return jogada
        else:
            print("Jogada inválida, Refaça sua jogada!")


def escolher_jogada_do_computador():
    return random.choice(opcoes_jokenpo())


def vencedor(jogada_do_usuario, jogada_computador):
    if jogada_do_usuario == jogada_computador:
        return 'Empate'
    if jogada_do_usuario == 'Pedra' and jogada_computador == 'Papel':
        return 'Computador venceu!'
    if jogada_do_usuario == 'Papel' and jogada_computador == 'Tesoura':
        return 'Computador venceu!'
    if jogada_do_usuario == 'Tesoura' and jogada_computador == 'Pedra':
        return 'Computador venceu!'
    else:
        return 'Você venceu!!'


while True:
    jogada_usuario = escolher_jogada_do_usuario()
    jogada_do_computador = escolher_jogada_do_computador()
    print('Você jogou', jogada_usuario)
    print('Computador jogou', jogada_do_computador)
    print(vencedor(jogada_usuario, jogada_do_computador))
    jogar_novamente = input('Deseja jogar novamente?  (s/n): ')
    if jogar_novamente.lower() != 's':
        break




