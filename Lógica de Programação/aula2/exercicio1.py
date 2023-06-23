print("Descubra a ordem crescente dos números!")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 != n2:

    if n1 > n2:
        print("A ordem crescente é:", n2, n1)
    else:
        print("A ordem crescente é:", n1, n2)
else:
    print("ERRO! Números iguais, digite números diferentes!")