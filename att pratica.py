class Pokemon:
    def __init__(self, nome):
        self.nome = nome
    def atacar(self):
        print(f"{self.nome} vai atacar!")
    def defender(self):
        print(f"{self.nome} vai defender!")

class Fogo(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
    def atacar(self):
        print(f"{self.nome} vai lançar um ataque de fogo!")   
    def defender(self):
        print(f"{self.nome} vai se proteger com uma barreira de fogo!")

class Agua(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
    def atacar(self):
        print(f"{self.nome} vai lançar um jato d'água!")
    def defender(self):
        print(f"{self.nome} vai se proteger com uma onda de água!")

class Planta(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
    def atacar(self):
        print(f"{self.nome} vai atacar com vinhas!")
    def defender(self):
        print(f"{self.nome} vai se proteger com folhas!")

def batalhar(pokemon1, pokemon2):
    print(f"\n{pokemon1.nome} vs {pokemon2.nome}\n")
    pokemon1.atacar()
    pokemon1.defender()
    pokemon2.atacar()
    pokemon2.defender()

pok1 = Fogo("Charmander")
pok2 = Agua("Squirtle")
pok3 = Planta("Bulbasaur")

batalhar(pok1, pok2)
batalhar(pok2, pok3)
batalhar(pok1, pok3)
