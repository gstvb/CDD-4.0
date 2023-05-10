def valor_total_estoque(nome_produto, quantidade, valor_unitario):
    valor_total = quantidade * valor_unitario
    return f"O valor total em estoque de {nome_produto} é de R${valor_total:.2f}"

print(valor_total_estoque("Leite", 10, 2.5))
print(valor_total_estoque("Arroz", 5, 6.0))
print(valor_total_estoque("Feijão", 3, 9.99))