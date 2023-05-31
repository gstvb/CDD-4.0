class Forma:

    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro


class Retangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)

    def CalcularArea(self, altura, base):
        self.altura = altura
        self.base = base
        calc = self.base * self.altura
        return calc

    def CalcularPerimetro(self, altura, base):
        self.altura = altura
        self.base = base
        calc = 2 * (self.base + self.altura)
        return calc




