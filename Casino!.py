import random

saldo = 100
def menu():
    global saldo
    while True:
        print("\n Bem-vindo ao Casino ")
        print(f"Saldo atual: {saldo} pontos")
        print("1 - Slot Machine")
        print("2 - Black Jack")
        print("3 - Sair")
        escolha = input("Escolha um jogo (1/2) ou saia (3): ")

        if escolha == "1":
            slt()
        elif escolha == "2":
            bj()
        elif escolha == "3":
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Escolha inválida. Tente novamente.")


def slt():
    global saldo
    print("\n Slot Machine ")
    aposta = int(input("Quantos pontos deseja apostar? "))

    if aposta > saldo:
        print("Saldo insuficiente!")
        return

    saldo -= aposta
    numeros = [random.randint(1, 5) for _ in range(3)]
    print(f"Números sorteados: {numeros}")

    if numeros[0] == numeros[1] == numeros[2]:
        print(" Triplo!!! Você ganhou 100 pontos!")
        saldo += 100
    elif numeros[0] == numeros[1] or numeros[1] == numeros[2] or numeros[0] == numeros[2]:
        print(" Dupla! Você ganhou 5 pontos!")
        saldo += 5
    else:
        print(" Nenhum número repetido! Você perdeu.")


def bj():
    global saldo
    print("\n Black Jack ")

    if saldo <= 0:
        print("Você não tem saldo suficiente para jogar.")
        return

    aposta = int(input("Quantos pontos deseja apostar? "))

    if aposta > saldo:
        print("Saldo insuficiente!")
        return

    saldo -= aposta
    P = random.randint(2, 10)
    print(f"Você começou com {P} pontos.")

    while P < 21:
        escolha = input("Deseja comprar mais uma carta? (s/n): ").strip().lower()
        if escolha == "s":
            nova_carta = random.randint(2, 10)
            P += nova_carta
            print(f"Você comprou uma carta de {nova_carta}. Total: {P}")
        else:
            break

    if P > 21:
        print(" Você ultrapassou 21! Perdeu a rodada.")
        return

    BP = random.randint(15, 21)
    print(f"A banca tem {BP} pontos.")

    if P > BP:
        print(" Você venceu! Ganhou o dobro da aposta!")
        saldo += aposta * 2
    elif P == BP:
        print(" Empate! Sua aposta foi devolvida.")
        saldo += aposta
    else:
        print(" Você perdeu para a banca.")


menu()
