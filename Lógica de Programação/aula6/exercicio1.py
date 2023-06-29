alunos_turma = []
alunos = int(input("Quantos alunos tem na turma: "))
for c in range (alunos):
    alunos_turma.append(input("Digite o nome do aluno: "))
for j in range(alunos) :
    print(j, alunos_turma[j])