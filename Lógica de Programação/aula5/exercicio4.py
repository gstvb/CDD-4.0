opcao = 0
soma = 0
subtração = 0
multiplicacao = 0
divisao = 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Selecione a operação: ")
print(" 1. Para soma","\n","2. Para subtração","\n","3. Para multiplicação","\n","4. Para divisão","\n","5. Para digitar novo número","\n","6. Para sair")
opcao = int(input("Digite a opção: "))

while opcao == 5:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("Selecione a operação: ")
    print(" 1. Para soma","\n","2. Para subtração","\n","3. Para multiplicação","\n","4. Para divisão","\n","5. Para digitar novo número","\n","6. Para sair")
    opcao = int(input("Digite a opção: "))

    while opcao != 6:
        if opcao == 1:
            soma = num1 + num2
            print(soma)
        elif opcao == 2:
            subtração = num1 - num2
            print(subtração)
        elif opcao == 3:
            multiplicacao = num1 * num2
            print(multiplicacao)
        elif opcao == 4:
            divisao = num1 / num2
            print(divisao)
    else:
            print("Programa encerrado.")
