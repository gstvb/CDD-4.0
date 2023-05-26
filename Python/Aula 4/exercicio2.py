class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O{self.nome} foi comer.")

    def emitir_som(self):
        print(f"O {self.nome} está emitindo som.")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está miando.")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está latindo.")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)



p1 = Gato("Lucian", "Preto")
p2 = Cachorro("Jorge", "Preto")
p3 = Vaca("Africana", "Laranja")
p1.emitir_som()
p2.emitir_som()
p3.emitir_som()
