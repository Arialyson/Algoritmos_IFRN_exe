#Questão_01

for c in range(1, 101):
    print(c, end=" ")

#Questão_02

for c in range(100, -1, -1):
    print(c, end=' ')

#Questão_03

n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))
for c in range(n1, n2+1):
    print(c)

#Questão_04

soma = 0

for c in range(1, 11):
    n = int(input("Digite um valor: "))
    soma += n
print(f"A soma é {soma}")

#Questão_05

soma = 0 

for c in range(1, 6):
    n = int(input("Valor: "))
    if n < 10:
        soma += n
print(f"A soma dos valores menores que dez é {soma}")