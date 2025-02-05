maior = 0
soma = 0
list = []

for cont in range(6):
    valor = float(input("Digite um número: ")) 
    list.append(valor)

soma = sum(list)
media = soma / len(list)

for cont2 in list:
    if cont2 > media:
        maior += 1

print("Soma:", soma)
print("Média:", media)
print("Quantidade de números maiores que a média:", maior)
