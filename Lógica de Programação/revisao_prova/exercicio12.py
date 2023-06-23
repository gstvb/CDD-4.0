"""

eleitores = int(input("Qual o número total de leitores? "))
votosbrancos = int(input("Quantos votaram branco? "))
votosnulos = int(input("Quantos votaram nulo? "))
votosvalidos = int(input("Quantos votos foram válidos? "))

percentual_brancos = votosbrancos / eleitores * 100
percentual_nulos = votosnulos / eleitores * 100
percentual_validos = votosvalidos / eleitores * 100

print(f"{percentual_brancos}%")
print(f"{percentual_nulos}%")
print(f"{percentual_validos}%")

"""

eleitores = int(input("Digite o número total de eleitores: "))
brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))

percent_brancos = (brancos / eleitores) * 100
percent_nulos = (nulos / eleitores) * 100
percent_validos = (validos / eleitores) * 100

print("Percentual de votos brancos: {:.2f}%".format(percent_brancos))
print("Percentual de votos nulos: {:.2f}%".format(percent_nulos))
print("Percentual de votos válidos: {:.2f}%".format(percent_validos))