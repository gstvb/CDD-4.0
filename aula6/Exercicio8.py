a = []
b = []
soma_vetores = []
soma = 0


for j in range(1):
    a.append(int(input("Digite três números: ")))
    b.append(int(input("Digite três números: ")))


for c in range(1):
    soma = a[c] + b[c]
    soma_vetores.append(soma)
print(a)
print(b)
print(soma_vetores)