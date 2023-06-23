"""
Escreva um algoritmo que receba do
usuário 10 números e mostre:
1. todos os números ímpares;
2. todos os números pares;
3. todos os números positivos;
4. todos os números negativos;
5. todos os zeros que aparecem no array

"""
num = []

for c in range(5):
    num.append(int(input("Digite 5 numeros: ")))

for j in range(5):
    if num[j] % 2 != 0:
        print('Numero impar: ', num[j], end=' ')

for f in range(5):
    if num[f] % 2 == 0:
        print('Numero par: ', num[f], end=' ')

for y in range(5):
    if num[y] > 0:
        print('Numero positivo: ', num[y], end=' ')

for t in range(5):
    if num[t] < 0:
        print('Numero negativo: ', num[t], end=' ')

for x in range(5):
    if num[x] == 0:
        print('Zero: ', num[x], end=' ')