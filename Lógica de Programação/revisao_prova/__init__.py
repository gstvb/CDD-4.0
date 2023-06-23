a = []
soma = 0

for x in range(4):
    a.append(float(input("Digite um número: ")))

for y in range(4):
    soma += a[y]

media = soma/4

print("A média é", media)
