idade_anos = int(input("Digite sua idade expressa em anos: "))
idade_meses = int(input("Quantos meses: "))
idade_dias = int(input("Quantos dias: "))

anos_idade = idade_anos * 365
anos_meses = idade_meses * 30

soma = anos_meses + anos_idade + idade_dias
print(f"Sua idade em dias: {soma}")



