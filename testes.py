soma = 0

# for c in range(1, 6):
#     n = int(input(f"Digite o {c}º número: "))
#     soma += n
# print(f'A soma dos valores é igual a {soma}')

lista = []

for c in range(1, 6):
    num = str(input("Digite um nome: "))
    if num not in lista:
        lista.append(num)
print(lista)
print("Hello")

for c in range(1, 11):
    print("Olá, mundo!")

lista = []

for c in range(1, 6):
    n = str(input("Digite algo: "))
    lista.append(n)
    
print(lista)