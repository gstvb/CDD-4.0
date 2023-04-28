nomes = []
senhas = []

for c in range(5):
    nomes.append(input("Digite seu nome: "))
    senhas.append(input("Digite sua senha: "))

for j in range(5):
    print(j, nomes[j], senhas[j])

'''
Quando for necessário imprimir somente o índice, vamos imprimir o índice do for, exemplo: print(j) 
quando for necessário mostrar o conteúdo do vetor, fica da seguinte forma: print(nomes[j])
'''

