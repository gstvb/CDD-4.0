import os
import random


jogar_de_novo = "sim"
numero_de_jogadas = 0
jogador = 1
numero_max_jogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def tela():
    os.system("cls")
    print("   0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   ___________")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   ___________")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(numero_de_jogadas))


def jogadas():
    global numero_de_jogadas
    global jogador
    global numero_max_jogadas

    if jogador == 1 and numero_de_jogadas < numero_max_jogadas:
        try:
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
            while velha[l][c] != " ":
                l = int(input("Linha..:"))
                c = int(input("Coluna.:"))
            velha[l][c] = "X"
            jogador = 2
            numero_de_jogadas += 1
        except:
            print("Jogada inválida.")
            os.system("Pause")


def cpu():
    global numero_de_jogadas
    global jogador
    global numero_max_jogadas

    if jogador == 2 and numero_de_jogadas < numero_max_jogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        numero_de_jogadas += 1
        jogador = 1


def verificar_vitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # Verificar Linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic <3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma ==3:
                vitoria = s
                break
            il +=1
        if vitoria != "n":
            break
        # Verificar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1
        if vitoria != "n":
            break
        # Diagonal 1
        soma = 0
        idiagl = 0
        idiagc = 2

        while idiagc >= 0:
            if velha[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global numero_de_jogadas
    global jogador
    global numero_max_jogadas
    global vit
    numero_de_jogadas = 0
    jogador = 1
    numero_max_jogadas = 9
    vit = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while jogar_de_novo == "sim":
    while True:
        tela()
        jogadas()
        cpu()
        vit = verificar_vitoria()
        if vit != "n" or numero_de_jogadas >= numero_max_jogadas:
            break
    print("Fim de jogo.")
    if vit == "X" or vit == "O":
        print(f"Resultado: Jogador {vit} venceu.")
    else:
        print("Resultado: Empate.")
    jogar_de_novo = input("Deseja jogar de novo? [sim/não]: ").lower()
    redefinir()