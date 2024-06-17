#Programa que simula o jogo de dados Craps e grava os resultados em um arquivo texto.

import random
import time

nomeJogador = []
valorAposta = []
resultado = []

# Função para lançar os dados
def lancar_dados():
    dadoA = random.randint(1, 6)
    time.sleep(1)
    dadoB = random.randint(1, 6)
    return dadoA, dadoB

def grava_dadosPartida():
    with open("craps.txt", "w") as arq:
        for nj, va, res in zip(nomeJogador, valorAposta, resultado):
            arq.write(f"{nj};{va};{res}\n")

# Início do jogo

while True:
    nj = input("Insira seu nome: ")
    va = float(input("Insira o valor da aposta: "))
    nomeJogador.append(nj)
    valorAposta.append(va)

    # Fazendo uma jogada dos dados
    dadoA, dadoB = lancar_dados()
    res = dadoA + dadoB
    resultado.append(res)

    print(f"O resultado do lançamento do dado A é: {dadoA}")
    time.sleep(2)
    print(f"O resultado do lançamento do dado B é: {dadoB}")
    time.sleep(2)
    print(f"O resultado do lançamento dos dados é: {resultado} (Jogador: {nomeJogador})")
    time.sleep(2)

    # Verificar se o jogador ganhou ou perdeu
    if resultado == 7 or resultado == 11:
        print("Você ganhou!")
        break
    elif resultado == 2 or resultado == 3 or resultado == 12:
        print("Você perdeu!")
        break
    else:
        # Continuar jogando até obter um resultado igual ao resultado anterior ou 7
        while True:
            input("Pressione Enter para jogar os dados novamente...")
            dadoA, dadoB = lancar_dados()
            novoResultado = dadoA + dadoB
            print(f"O resultado do lançamento do dado A é: {dadoA}")
            time.sleep(2)
            print(f"O resultado do lançamento do dado B é: {dadoB}")
            time.sleep(2)
            print(f"O resultado do lançamento dos dados é: {novoResultado} (Jogador: {nomeJogador})")
            time.sleep(2)

            if novoResultado == resultado:
                print("Você ganhou!")
                break
            elif novoResultado == 7:
                print("Você perdeu!")
                break

        opcao = input("Aperte 'x' para encerrar o jogo ou 'r' para jogar novamente: ")
        if opcao == 'x':
            grava_dadosPartida()
            break
        elif opcao == 'r':
            continue
        else:
            print("Opção inválida. O jogo será encerrado.")
            grava_dadosPartida()
            break

##Verificar quem ganhou ou perdeu txt