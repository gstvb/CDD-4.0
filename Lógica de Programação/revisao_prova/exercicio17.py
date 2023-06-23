macas = int(input("Quantas maçãs você deseja comprar? "))

if macas < 12:
    menos = macas * 1.30
    print(f"Vai custar: R$ {menos}")
else:
    mais = macas * 1.00
    print(f"Vai custar: R$ {mais}")