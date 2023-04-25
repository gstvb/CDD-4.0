soma = 0
acima_media = 0
notas_alunos = []

for c in range(5):
    notas_alunos.append(float(input("Digite as notas dos alunos: ")))

for x in range(5):
    soma = soma + notas_alunos [x]
media = soma/5

for y in range(5):
    if notas_alunos[y] > media:
        acima_media += 1

print("Média da turma: ", media)
print("Alunos acima da média: ", acima_media)








