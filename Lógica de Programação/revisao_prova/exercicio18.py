"""
Escreva um algoritmo que dado um
arrays, retorno um novo array, com os
elementos em ordem invertida.
entrada:
a=[2,5,4,2,8,5,2]
saída
b=[2,5,8,2,4,5,2]
"""

a = [1, 2, 3, 4, 5, 6, 7]
b = []

for j in range(-6, -1, -1):
    b.append(a[j])

print(b)
