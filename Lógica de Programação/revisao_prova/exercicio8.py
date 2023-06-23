"""
num1 = int(input("Digite o primeiro: "))
num2 = int(input("Digite o segundo: "))
num3 = int(input("Digite o terceiro: "))
num4 = int(input("Digite o quarto: "))

soma = num1 + num2 + num3 + num4
media = soma / 4

print(media)
"""
a = []
soma = 0

for x in range(4):
    a.append(float(input("Digite um número: ")))

for y in range(4):
    soma += a[y]

media = soma/4

print("A média é", media)
