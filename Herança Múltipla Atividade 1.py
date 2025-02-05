class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def imprimir_potencia(self):
        print(f"Potência: {self.potencia}")

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def imprimir_dados_veiculo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Caminhao(Motor, Veiculo):
    def __init__(self, marca, modelo, potencia, toneladas, altura_max, comprimento):
        Motor.__init__(self, potencia)
        Veiculo.__init__(self, marca, modelo)
        self.toneladas = toneladas
        self.altura_max = altura_max
        self.comprimento = comprimento
    
    def imprimir_dados_caminhao(self):
        self.imprimir_dados_veiculo()
        self.imprimir_potencia()
        print(f"Toneladas: {self.toneladas}")
        print(f"Altura máxima: {self.altura_max}")
        print(f"Comprimento: {self.comprimento}")

caminhao1 = Caminhao("Scania", "R450", 350, 18, 4, 12)
caminhao1.imprimir_dados_caminhao()
