valor = int(input("Escreva um número inteiro: "))

if valor >= 1:
    for x in range(1, valor+1):
        print(x)
else:
    print("Digite um valor maior que 0!")
