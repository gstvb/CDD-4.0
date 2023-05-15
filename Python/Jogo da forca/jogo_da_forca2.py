import random

palavras = ['python', 'banana', 'jogos', 'escola', 'peixe', 'janela', 'carros', 'limite', 'templo', 'tigres']

palavra_secreta = random.choice(palavras)

print(f'A palavra tem {len(palavra_secreta)} letras.')
letras_certas = []
letras_erradas = []
erros = 0

while True:
    letra = input("Digite uma letra ou adivinhe a palavra secreta: ").lower()

    if len(letra) == len(palavra_secreta):
        if letra == palavra_secreta:
            print("Parabéns, você acertou a palavra secreta:", palavra_secreta)
            break
        else:
            print("Você errou a palavra secreta.")
            letras_erradas.append(letra)

    if letra in letras_certas or letra in letras_erradas:
        print('Você já tentou essa letra.')
    elif letra in palavra_secreta:
        print('Acertou!')
        letras_certas.append(letra)
    else:
        print(f'Errou. A palavra não contém a letra "{letra}".')
        letras_erradas.append(letra)
        erros += 1

        if erros == 3:
            print('Fim de jogo. Você perdeu!')
            print(f'A palavra secreta era "{palavra_secreta}".')
            break

    palavra_para_mostrar = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_para_mostrar += letra_secreta
        else:
            palavra_para_mostrar += '_'

    print(palavra_para_mostrar)

    if palavra_para_mostrar == palavra_secreta:
        print('Parabéns! Você ganhou!')
        break
