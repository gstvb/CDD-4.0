a = []
m = []
mult = 0



for c in range(10):
    a.append(int(input("Digite 10 números: ")))

x = int(input("Digite o multiplicador: "))

for j in range(10):
   mult =  a[j] * x
   m.append(mult)
print(a)
print(x)
print(m)
