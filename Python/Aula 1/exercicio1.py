
def somar( num1, num2):
    soma = num1 + num2
    print(f"Resultado da soma é: {soma}")

def subtrair(num1, num2):
    sub = num1 - num2
    print(f"Resultado da soma é: {sub}")

def multiplicar(num1, num2):
    mult = num1 * num2
    print(f"Resultado da multiplicação é: {mult}")

def dividir(num1, num2):
    div = num1 / num2
    print(f"Resultado da multiplicação é: {div}")


while True:

    print("""
    Menu :
    
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair
    """)

    num1 = int(input("Digite um número:"))
    num2 = int(input("Digite um número:"))

    operacao = int(input("Escolha um número referente a uma das operações: "))


    if operacao == 1:
        somar(num1,num2)

    elif operacao == 2:
        subtrair(num1,num2)

    elif operacao == 3:
        multiplicar(num1,num2)

    elif operacao == 4:
        dividir(num1,num2)

    else:
        print("Programa encerrado.")
        break
