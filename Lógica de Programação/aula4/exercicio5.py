pin = "123"
tentativas = 0
senha = input("Digite sua senha: ")
while senha != pin and tentativas < 2:
    print("Senha incorreta, digite novamente: ")
    senha = input()
    tentativas = tentativas + 1
if senha == pin:
    print("Aguarde, acessando sua conta...")
else:
    print("Senha bloqueada!")