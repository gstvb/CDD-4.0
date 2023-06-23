""""
Usando While escreva um algoritmo
que preencha um array A com os 10
primeiros números ímpares, iniciando por
zero.

"""
a = []
num = 0
cont = 0

while cont < 20:
    if num % 2 != 0:
        a.append(num)
    num += 1
    cont += 1
print(a)