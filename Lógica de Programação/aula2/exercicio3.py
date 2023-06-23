time1 = input("Digite o nome do time 1: ")
time2 = input("Digite o nome do time 2: ")
golTime1 = float(input("Digite a quantidade de gols marcados pelo time 1: "))
golTime2 = float(input("Digite a quantidade de gols marcados pelo time 2: "))
if golTime1 != golTime2:

    if golTime1 > golTime2:
        print("Gols do time", time1, ":", golTime1)
        print("Gols do time", time2, ":", golTime2)
        print("O vencedor foi o", time1)
    else:
        print("Gols do time", time1, ":", golTime1)
        print("Gols do time", time2, ":", golTime2)
        print("O vencedor foi o time ", time2)
else:
    print("Gols do time", time1, ":", golTime1)
    print("Gols do time", time2, ":", golTime2)
    print("Houve empate!")
