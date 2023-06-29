numeros = []
soma = 0
media = 0

for c in range(10):
    numeros.append(int(input("Digite 10 números: ")))

maior = numeros[0]
menor = numeros[0]

for y in range(10):
    if numeros[y] > maior:
        maior = numeros[y]
    if numeros[y] < menor:
        menor = numeros[y]
print("O maior número é: ", maior)
print("O menor número é: ", menor)
for j in range(10):
    if numeros[j] %2 == 0:
        print(numeros[j], end=' ')

for h in range(10):
    soma+= numeros[j]
    print(soma)
    media = soma/10
print(media)

for x in range(10):
    if numeros[x] > media:
        print(numeros[x], end=' ')
