class Banco:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    
    def Imprimir_Info(self):
        return f'Banco: {self.nome}\nEndereço: {self.endereco}'

class ContaDoBanco(Banco):
    def __init__(self, nome, endereco, cliente, num_conta, saldo):
        super().__init__(nome, endereco)
        self.cliente = cliente
        self.num_conta = num_conta
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f'Saque de {valor} realizado. Novo saldo: {self.saldo}'
        else:
            return 'Saldo insuficiente.'
        
    def depositar(self, valor):
        self.saldo += valor
        return f'Depósito de {valor} realizado. Novo saldo: {self.saldo}'

    def consultar_saldo(self):
        return f'Saldo atual: {self.saldo}'

class ContaPoupanca(ContaDoBanco):
    def __init__(self, nome, endereco, cliente, num_conta, saldo, taxa_rendimento):
        super().__init__(nome, endereco, cliente, num_conta, saldo)
        self.taxa_rendimento = taxa_rendimento
        
    def Calcular_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento
        return f'O rendimento de {rendimento} foi calculado. Novo saldo: {self.saldo}'

class ContaEspecial(ContaDoBanco):
    def __init__(self, nome, endereco, cliente, num_conta, saldo, limite):
        super().__init__(nome, endereco, cliente, num_conta, saldo)
        self.limite = limite
    
    def Imprimir_limite(self):
        return f'O limite da conta especial é: {self.limite}'

conta_especial = ContaEspecial(
    nome="BB",
    endereco="Rua Camões, 345, Curitiba",
    cliente="Rodrigo Santoro",
    num_conta="345-6",
    saldo=2000,
    limite=10000
)

conta_poupanca = ContaPoupanca(
    nome="Caixa",
    endereco="Rua Marista, 33, Pinhais",
    cliente="Leonardo DiCaprio",
    num_conta="234-9",
    saldo=5400,
    taxa_rendimento=0.1
)
print("\n=====================================\n")
print("Conta Poupança:")
print(conta_poupanca.Imprimir_Info())
print(conta_poupanca.sacar(1000))
print(conta_poupanca.Calcular_rendimento())
print(conta_poupanca.consultar_saldo())
print("\n=====================================\n")

print("Conta Especial:")
print(conta_especial.Imprimir_Info())
print(conta_especial.consultar_saldo())
print(conta_especial.Imprimir_limite())
print(conta_especial.depositar(350))
print(conta_especial.consultar_saldo())
print("\n=====================================\n")
