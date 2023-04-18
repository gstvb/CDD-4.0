aluno = int(input("Digite a quantidade de alunos: "))
soma = 0
x = 1
while x <= aluno:
    nota = float(input("Digite a nota do aluno: "))
    soma = soma + nota
    x = x + 1
media = soma/aluno
print("A média da turma é: ", media)