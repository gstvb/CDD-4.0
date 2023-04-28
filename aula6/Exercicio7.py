nomes = []
senhas = []
cont = 0


for c in range(2):
    nomes.append(input("Digite seu nome: "))
    senhas.append(input("Digite sua senha: "))
login = input("Digite o login: ")
senha = input("Digite a senha: ")


for j in range(2):
    if login == nomes[j] and senha == senhas[j]:
        print("Usuário logado. ")
        break
    else:
        cont+=1
if cont ==2:
    print("Login ou senha incorretos. ")


