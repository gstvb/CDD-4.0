class Atleta:

    def __init__(self, peso):
        self.peso = peso
        self.aposentar = False
        self.aquecendo = False
        self.correndo = False
        self.nadando = False
        self.pedalando = False


    def aquecer(self):
        if self.aposentar == False:
            self.aquecendo = True
            return "O atleta está aquecendo."
        return "O atleta não está mais em atividade"

    def correr(self):
        if self.aposentar == False and self.aquecendo == True:
            self.correndo = True
            return "O Atleta está correndo"
        return "O Atleta precisa aquecer antes de correr."

    def nadar(self):
        if self.aposentar != True and self.aquecendo != False:
            if self.correndo == False:
                self.nadando = True
                return "O atleta está nadando."
        return "O atleta não pode nada agora."

    def


class Corredor:

    def __init__(self, peso, aposentar):
        super().__init__(peso, aposentar)

class Nadador
class Ciclista

