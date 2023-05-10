def contar_vogais(texto):
    cont = 0
    vogais = "aeiouAEIOU"

    for x in texto:
        if x in vogais:
            cont += 1
    return cont
texto = input("Digite um texto: ")
print("O texto tem", contar_vogais(texto), "vogais")









