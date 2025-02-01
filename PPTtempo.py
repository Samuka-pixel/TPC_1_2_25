from random import randint
from time import  sleep

X = ("Sim")
while X == "Sim":
    Op = str(input("Pedra papel or tesoura?: "))
    list = ["Pedra", "Papel", "Tesoura"]
    rand = randint(0, 2)
    sleep(5)
    print(list[rand])
    if Op == "pedra":
        if rand == 0:
            print("Empate")
        elif rand == 1:
            print("Perdeste!")
        elif rand == 2:
            print("Ganhaste")
        else:
            print("erro")
    elif Op == "papel":
        if rand == 1:
            print("Empate")
        elif rand == 2:
            print("Perdeste!")
        elif rand == 0:
            print("Ganhaste")
        else:
            print("erro")
    elif Op == "tesoura":
        if rand == 2:
            print("Empate")
        elif rand == 0:
            print("Perdeste!")
        elif rand == 1:
            print("Ganhaste")
        else:
            print("erro")
    else:
        print("erro")
    X = str(input("Conitnuar?: "))
