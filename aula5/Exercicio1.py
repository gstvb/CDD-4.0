exit = "s"
while exit == "s":
    n1 = float(input("Digite a primeira nota do aluno: "))
    while n1 < 0 or n1 > 10:
        print("As notas devem ser de 0 a 10! Informe a nota do aluno novamente:")
        n1 = float(input())
    n2 = float(input("Digite a segunda nota do aluno: "))
    while n2 < 0 or n2 > 10:
        print("As notas devem ser de 0 a 10! Informe a nota do aluno novamente:")
        n2 = float(input())
    media = (n1 + n2) / 2
    print("A média do aluno é:", media)
    exit = input("Deseja continuar?(s/n) ")