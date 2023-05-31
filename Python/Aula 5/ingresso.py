class Ingresso:

    def __init__(self, valor):
        self.valor = valor

    def ImprimeValor(self):
        print(f"O valor do ingresso é: R$ {self.valor}")

class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        calc = (self.adicional / self.valor) * 100
        return calc

ingresso = Ingresso(80)
ingresso.ImprimeValor()

IngressoVIP = VIP(25, 100)
print(f"Valor do ingresso VIP: R${valorVIP()}")
