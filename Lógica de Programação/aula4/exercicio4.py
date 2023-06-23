n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
resultado = 0
while n2 == 0:
    print("Digite um número diferente de 0")
    n2 = float(input("Digite um numero diferente de 0: "))
else:
    resultado = n1/n2
    print(resultado)
