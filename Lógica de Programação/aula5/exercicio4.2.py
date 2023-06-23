resp = 0

while resp !=6:
    num1= int(input("Digite o primeiro número: "))
    num2= int(input("Digite o segundo número: "))

    while True:
        resp = int(input("Digite 1 para somar \n"
                             "Digite 2 para Subtrair \n"""
                             "Digite 3 para Multiplicar\n"
                             "Digite 4 para Dividir\n"
                             "Digite 5 para Digitar novo número \n"
                             "Digite 6 para Para sair\n"))
        match resp:
            case 1:
                print(num1+num2)
            case 2:
                print(num1-num2)
            case 3:
                print(num1*num2)
            case 4:
                print(num1/num2)
            case 5:
                break

            case 6:
                print("Programa encerrado.")