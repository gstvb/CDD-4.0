nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
salario = float(input("Digite seu salário: "))
aumento = float(input("Digite a % do seu aumento: "))
total = ((aumento * salario)/100) + salario
print("Nome:", nome, "\nIdade:", idade, "\nSalário:", salario, "\nSalário após o aumento:", total)