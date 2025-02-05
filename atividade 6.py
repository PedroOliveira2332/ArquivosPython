list = []

for i in range(10):
    elemento = input("Digite um elemento: ")
    list.append(elemento)

numero = input("Digite um número para verificar se pertence à lista: ")

if numero in list:
    print(f"O número {numero} pertence à lista.")
else:
    print(f"O número {numero} não pertence à lista.")