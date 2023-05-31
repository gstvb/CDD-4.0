class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor:.2f}")


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional

ingresso = Ingresso(100)
ingresso.imprimeValor()


ingressoVIP = VIP(30, 10)
print(f"Valor do ingresso VIP: R${ingressoVIP.valorVIP():.2f}")
