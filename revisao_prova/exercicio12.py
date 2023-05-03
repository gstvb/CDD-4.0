eleitores = int(input("Qual o número total de leitores? "))
votosbrancos = int(input("Quantos votaram branco? "))
votosnulos = int(input("Quantos votaram nulo? "))
votosvalidos = int(input("Quantos votos foram válidos? "))

percentual_brancos = (eleitores * votosbrancos) / 100
percentual_nulos = eleitores * votosnulos / 100
percentual_validos = eleitores * votosvalidos / 100

print(f"{percentual_brancos}%")
print(f"{percentual_nulos}%")
print(f"{percentual_validos}%")