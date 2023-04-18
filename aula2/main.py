"""forma que o professor fez"""
tipo = input("Tipos de  combustíveis: \nE-etanol ou \nG-galosina \nInforme sua escolha: ")
litros = float(input("Informe quantos litros: "))

if tipo in "Gg" or tipo in "Ee":

    if tipo in "Gg":
        valor = litros * 5.80
        print("O valor gasto foi:", valor)
    else:
        valor = litros * 4.90
        print("O valor gasto foi:", valor)
else:
    print("Valor inválido!")