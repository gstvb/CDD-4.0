print("Descubra se um número é par ou ímpar!")
numero = float(input("Digite um número: "))
if numero != 0:
    if numero % 2 == 0:
        print("O número", numero, "é par!")
    else:
        print("O número", numero, "é ímpar!")
else:
    print("Escreva um número diferente de zero!")