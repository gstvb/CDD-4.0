nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Nota final do aluno foi:", media)
    print("APROVADO!")
elif media >= 4:
    print("Nota final do aluno foi:", media)
    print("RECUPERAÇÃO!")
else:
    print("Nota final do aluno foi:", media)
    print("REPROVADO!")
