#Questão_01 -----------------------------------------------------------------------------

for i in range(1, 101):
    print(i)

#Questão_02 ------------------------------------------------------------------------------

for i in range(100, 0, -1):
    print(i)

#Questão_03 -------------------------------------------------------------------------------

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma = 0

if inicio > fim:
    inicio, fim = fim, inicio

print("Números no intervalo:")
for i in range(inicio, fim + 1):
    print(i, end=" ")
    soma += i

print(f"\nSomatório do intervalo: {soma}")

#Questão_04 ---------------------------------------------------------------------------------

soma = 0
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num

print(f"O somatório dos números é: {soma}")

#Questão_05 -----------------------------------------------------------------------------------

soma = 0
for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if valor < 10:
        soma += valor

print(f"O somatório dos valores menores que 10 é: {soma}")


#Questão_06 -----------------------------------------------------------------------------------

soma = 0
for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if 10 <= valor < 20:
        soma += valor

print(f"O somatório dos valores entre 10 e 19.99 é: {soma}")


#Questão_07 ------------------------------------------------------------------------------------

soma_pares = 0
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    if valor % 2 == 0:
        soma_pares += valor

print(f"O somatório dos números pares é: {soma_pares}")


#Questão_08 -------------------------------------------------------------------------------------

quantidade = int(input("Quantos valores você deseja digitar? "))
qtd_pares = 0

for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        qtd_pares += 1

print(f"Quantidade de números pares digitados: {qtd_pares}")


#Questão_09 -------------------------------------------------------------------------------------

soma_posicoes_impares = 0  # 1º, 3º, 5º, 7º, 9º
soma_posicoes_pares = 0    # 2º, 4º, 6º, 8º, 10º

for i in range(1, 11):
    valor = float(input(f"Digite o {i}º valor: "))
    if i % 2 != 0:
        soma_posicoes_impares += valor
    else:
        soma_posicoes_pares += valor

print(f"Soma das posições ímpares: {soma_posicoes_impares}")
print(f"Soma das posições pares: {soma_posicoes_pares}")

if soma_posicoes_impares > soma_posicoes_pares:
    print("O somatório dos números ímpares (em ordem de digitação) é MAIOR.")
elif soma_posicoes_impares < soma_posicoes_pares:
    print("O somatório dos números ímpares (em ordem de digitação) é MENOR.")
else:
    print("Os somatórios são IGUAIS.")


#Questão_10 --------------------------------------------------------------------------------------

soma_pares = 0
soma_impares = 0

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    if valor % 2 == 0:
        soma_pares += valor
    else:
        soma_impares += valor

print(f"Somatório dos números pares: {soma_pares}")
print(f"Somatório dos números ímpares: {soma_impares}")

if soma_impares > soma_pares:
    print("O somatório dos números ímpares é MAIOR do que o dos pares.")
elif soma_impares < soma_pares:
    print("O somatório dos números ímpares é MENOR do que o dos pares.")
else:
    print("Os somatórios são IGUAIS.")


#Questão_11 ----------------------------------------------------------------------------------------

total = int(input("Digite o total de números a serem somados: "))
numeros = []
soma = 0

for i in range(total):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    soma += num

# Criando a string de saída unindo os números com '+'
equacao = "+".join(map(str, numeros))
print(f"Saída no terminal: {equacao}={soma}")


#Questão_12 ---------------------------------------------------------------------------------------

resultados = []

for i in range(1000, 3001):
    if i % 7 == 0 and i % 5 != 0:
        resultados.append(str(i))

# Junta todos os elementos da lista separando-os por ";"
print(";".join(resultados))


#Questão_13 -----------------------------------------------------------------------------------------

num = int(input("Entrada: "))

print("Saída: ", end="")
for i in range(1, 11):
    resultado = i * num
    print(f"{i}x{num}={resultado}", end="; ")
print()


#Questão_14 ----------------------------------------------------------------------------------------

n = int(input("Entrada: "))

print("Saída:")
# Parte crescente do triângulo
for i in range(1, n + 1):
    print("*" * i)

# Parte decrescente do triângulo
for i in range(n - 1, 0, -1):
    print("*" * i)


#Questão_15 ---------------------------------------------------------------------------------

pares = 0
impares = 0

while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break  # Interrompe o loop while imediatamente
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")


#Questão_16 ---------------------------------------------------------------------------------

n = int(input("Digite o valor de N: "))
resultados = []

for i in range(1, n + 1):
    if i % 3 == 0 and i % 7 == 0:
        resultados.append("POW")
    elif i % 3 == 0:
        resultados.append("PI")
    elif i % 7 == 0:
        resultados.append("PA")
    else:
        resultados.append(str(i))

print(", ".join(resultados))
