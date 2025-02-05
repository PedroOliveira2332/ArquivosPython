class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base
    
    def Salario_base(self):
        return self.salario_base
    
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus):
        super().__init__(nome, matricula, salario_base)
        self.bonus = bonus

    def Imprime_Info(self):
        return f"Nome: {self.nome}\nMatrícula: {self.matricula}\nSalário Base: R${self.salario_base:.2f}\nBônus: R${self.bonus:.2f}\n"

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, valor_vendido):
        super().__init__(nome, matricula, salario_base)
        self.valor_vendido = valor_vendido

    def Salario_total(self):
        comissao = 0.10 * self.valor_vendido
        return self.salario_base + comissao

vendedor1 = Vendedor("Carlos Silva", "V12345", 2000, 5000)
vendedor2 = Vendedor("Ana Souza", "V67890", 2200, 8000)

print("==========================================================================")
print(f"Salário total de {vendedor1.nome}: R${vendedor1.Salario_total():.2f}")
print(f"Salário total de {vendedor2.nome}: R${vendedor2.Salario_total():.2f}")
print("==========================================================================")