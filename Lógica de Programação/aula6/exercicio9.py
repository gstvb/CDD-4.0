numeros = []

for c in range(10):
    numeros.append(int(input("Digite 10 números: ")))
num = int(input("Digite outro número: "))
cont = 0
for j in range(10):
    if num == numeros[j]:
        cont+=1
print("O número se repete: ", cont)