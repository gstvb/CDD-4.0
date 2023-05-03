num = int(input('Digite um número: '))

if num % 2 == 0 and num > 0:
    print("Número par e positivo.")
elif num % 2 != 0 and num > 0:
    print("Número ímpar e positivo.")
elif num % 2 == 0 and num < 0:
    print("Número par e negativo")
else:
    print("Número ímpar e negativo.")
