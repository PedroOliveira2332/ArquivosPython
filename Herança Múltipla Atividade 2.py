class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir_informacoes_pessoa(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Curso:
    def __init__(self, nome_curso, codigo_curso):
        self.nome_curso = nome_curso
        self.codigo_curso = codigo_curso
    
    def imprimir_informacoes_curso(self):
        print(f"Curso: {self.nome_curso}")

class Notas:
    def __init__(self, nota_1, nota_2, nota_final):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_final = nota_final
    
    def imprimir_informacoes_notas(self):
        print(f"Nota 1: {self.nota_1}")
        print(f"Nota 2: {self.nota_2}")
        print(f"Nota final: {self.nota_final}")

class Estudante(Pessoa, Curso, Notas):
    def __init__(self, nome, idade, nome_curso, codigo_curso, nota_1, nota_2, nota_final):
        Pessoa.__init__(self, nome, idade)
        Curso.__init__(self, nome_curso, codigo_curso)
        Notas.__init__(self, nota_1, nota_2, nota_final)
    
    def mostrar_todas_informacoes(self):
        self.imprimir_informacoes_pessoa()
        self.imprimir_informacoes_curso()
        self.imprimir_informacoes_notas()

estudante1 = Estudante("João Silva", 20, "Engenharia de Software", "ES123", 8.5, 7.0, 9.0)
estudante1.mostrar_todas_informacoes()
