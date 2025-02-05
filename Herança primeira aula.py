class Animal:
    def __init__(self, nome, comprimento, numero_de_patas, cor, ambiente):
        self.nome = nome
        self.comprimento = comprimento
        self.numero_de_patas = numero_de_patas
        self.cor = cor
        self.ambiente = ambiente

    def Info(self):
        print(f"Nome: {self.nome}")
        print(f"Comprimento: {self.comprimento} cm")
        print(f"Número de patas: {self.numero_de_patas}")
        print(f"Cor: {self.cor}")
        print(f"Ambiente: {self.ambiente}")

class Peixe(Animal):
    def __init__(self, nome, comprimento, cor, ambiente, caracteristica):
        super().__init__(nome, comprimento, 0, cor, ambiente)
        self.caracteristica = caracteristica

    def Info_Peixe(self):
        self.Info()
        print(f"Característica: {self.caracteristica}")

class Mamifero(Animal):
    def __init__(self, nome, comprimento, numero_de_patas, cor, ambiente, alimento):
        super().__init__(nome, comprimento, numero_de_patas, cor, ambiente)
        self.alimento = alimento

    def Info_Mam(self):
        self.Info()
        print(f"Alimento: {self.alimento}")

camelo = Mamifero(nome="Camelo", comprimento=150, numero_de_patas=4, cor="Amarelo", ambiente="Terra", alimento="leite")
tubarao = Peixe(nome="Tilápia", comprimento=20, cor="Cinzento", ambiente="Mar", caracteristica="cauda")
urso_canada = Mamifero(nome="Urso-do-canadá", comprimento=180, numero_de_patas=4, cor="Vermelho", ambiente="Terra", alimento="Mel")

print("=======================================")
print("Informações do Camelo (Mamífero): ")
print("=======================================")
camelo.Info_Mam()
print("\n=======================================")
print("Informações do Tubarão: ")
print("=======================================")
tubarao.Info_Peixe()
print("\n=======================================")
print("Informações do Urso: ")
print("=======================================")
urso_canada.Info_Mam()
