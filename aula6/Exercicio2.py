
quantidade = int(input("Digite a quantidade de alunos: "))
nomes_alunos = []

for c in range(quantidade):
    nomes_alunos.append(input("Digite o nome do aluno: "))

pesquisa = input("Digite um nome para pesquisa: ")
cont = 0

for j in range(quantidade):
    if pesquisa == nomes_alunos[j]:
        print(j, nomes_alunos[j])
    else:
        cont+= 1

if cont == quantidade:
        print("Not found. ")