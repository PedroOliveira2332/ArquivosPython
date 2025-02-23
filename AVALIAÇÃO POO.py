class Forma():
    def __init__(self, nome):
        self.nome = nome

class Esfera(Forma):
    def __init__(self, raio):
        super().__init__("esfera")
        self.raio = raio

    def calc_area(self):
        return 4 * 3.14 * self.raio ** 2  

    def exibir_area(self):
        print(f"A área da {self.nome} é: {self.calc_area():.2f} cm²")


class Trapezio(Forma):
    def __init__(self, b_menor, b_maior, altura):
        super().__init__("trapezio")
        self.b_menor = b_menor
        self.b_maior = b_maior
        self.altura = altura

    def calc_area(self):
        return ((self.b_maior + self.b_menor) * self.altura) / 2

    def exibir_area(self):
        print(f"A área do {self.nome} é: {self.calc_area():.2f} cm²")


class Cilindro(Forma):
    def __init__(self, raio, altura):
        super().__init__("cilindro")
        self.raio = raio
        self.altura = altura

    def calc_area(self):
        return 2 * 3.14 * self.raio * (self.raio + self.altura)

    def exibir_area(self):
        print(f"A área do {self.nome} é: {self.calc_area():.2f} cm²")


e1 = Esfera(7)
t1 = Trapezio(10, 6, 4)
c1 = Cilindro(3, 5)

e1.exibir_area()
t1.exibir_area()
c1.exibir_area()

print(e1)
print(t1)
print(c1)
