from time import sleep
com = str(input("Queres começar o jogo?\n"
                ">"))
Pontos = 0
if com == "Sim":
    print("Primeira pergunda")
    P1 = str(input("Quem é o Micheal Jackson?\n"
             "A) Um musico\n"
             "B) Um Politico\n"
             "C) Um Ator\n"
             "D) Um Chef\n"
             "----->"))
    if P1 == "A":
        print("Parabens")
        Pontos = Pontos + 1
    else:
        print("Errado :(")
        Pontos = 0
    print(f'Tens {Pontos} pontos, ou seja {Pontos * 1000000}€')
    print("Segunda pergunda")


    P3 = str(input("Quem é o Gordom Ramsey?\n"
             "A) Um musico\n"
             "B) Um Politico\n"
             "C) Um Ator\n"
             "D) Um Chef\n"
             "----->"))
    if P3 == "D":
        print("Parabens")
        Pontos = Pontos + 1
    else:
        print("Errado :(")
        Pontos = 0
    print(f'Tens {Pontos} pontos, ou seja {Pontos * 1000000}€')

    P3 = str(input("Quem é o Barack Obama?\n"
                   "A) Um musico\n"
                   "B) Um Politico\n"
                   "C) Um Ator\n"
                   "D) Um Chef\n"
                   "----->"))
    if P3 == "B":
        print("Parabens")
        Pontos = Pontos + 1
    else:
        print("Errado :(")
        Pontos = 0
    print(f'Tens {Pontos} pontos, ou seja {Pontos * 1000000}€')

    P4 = str(input("Quem é o Ryan Renolds?\n"
                   "A) Um musico\n"
                   "B) Um Politico\n"
                   "C) Um Ator\n"
                   "D) Um Chef\n"
                   "----->"))
    if P4 == "C":
        print("Parabens")
        Pontos = Pontos + 1
    else:
        print("Errado :(")
        Pontos = 0
    print(f'Tens {Pontos} pontos, ou seja {Pontos * 1000000}€')

    sleep(5)
    print(f'Parabens!! Ganhaste {Pontos} pontos!! E um total de {Pontos * 1000000}€!!!!')
else:
    print("OK, entao n jogas!")
