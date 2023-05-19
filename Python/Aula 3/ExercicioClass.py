
class Pessoas:

    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = comendo

    def comer(self, comida):
        self.comida = comida
        if self.comendo:
            print(f'{self.nome} já está comendo.')
        else:
            print(f'{self.nome} foi comer {self.comida}.')
            self.comida = True


    def parardecomer(self):
        if self.comendo == True:
            self.comendo = False
            print(f'{self.nome} parou de comer.')
        else:
            print(f'{self.nome} não está comendo.')

    def falar(self, falando):
        self.falando = False
        if falando == True:
            print(f'{self.nome} já está falando.')
        else:
            print(f'{self.nome} não está falando.')


    def parardefalar(self):

        if self.falando == True:
            if self.comendo == False:
                print(f'{self.nome} está falando, por isso não pode comer.')
        elif self.comendo == True and self.falando == True:
            print(f'{self.nome}, pare de falar, você está comendo.')
        else:
            print(f'{self.nome} está comendo, por isso não pode falar. ')



p1 = Pessoas("João", 80, 23, True)
p2 = Pessoas("Maria", 54, 19, False)

p1.comer("Banana")
p1.parardecomer()
p1.falar(True)
p1.parardefalar()

