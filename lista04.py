#exercício_01 -------------------------------------------------------------------------------

lista = [0] * 10

for i in range(10):
    lista[i] = int(input(f"Digite o valor {i+1}: "))

qtd_pares = 0
for i in range(10):
    if lista[i] != 0 and lista[i] % 2 == 0:
        qtd_pares += 1

print(f"Qtd valores par: {qtd_pares}")

#exercício_02 -------------------------------------------------------------------------------

tamanho = int(input("Defina o tamanho das listas: "))

lista1 = [0] * tamanho
lista2 = [0] * tamanho

print("Preenchendo a Lista 1:")
for i in range(tamanho):
    lista1[i] = int(input(f"Valor {i+1}: "))

print("Preenchendo a Lista 2:")
for i in range(tamanho):
    lista2[i] = int(input(f"Valor {i+1}: "))

soma_par1 = 0
soma_impar1 = 0
soma_par2 = 0
soma_impar2 = 0

for i in range(tamanho):
    if lista1[i] % 2 == 0:
        soma_par1 += lista1[i]
    else:
        soma_impar1 += lista1[i]

for i in range(tamanho):
    if lista2[i] % 2 == 0:
        soma_par2 += lista2[i]
    else:
        soma_impar2 += lista2[i]

print(f"Soma listaPar1: {soma_par1}")
print(f"Soma listaPar2: {soma_par2}")
if soma_par1 > soma_par2:
    print("listaPar1 > listaPar2")
elif soma_par1 < soma_par2:
    print("listaPar1 < listaPar2")
else:
    print("listaPar1 = listaPar2")

print(f"Soma listalmpar1: {soma_impar1}")
print(f"Soma listalmpar2: {soma_impar2}")
if soma_impar1 > soma_impar2:
    print("listalmpar1 > listalmpar2")
elif soma_impar1 < soma_impar2:
    print("listalmpar1 < listalmpar2")
else:
    print("listalmpar1 = listalmpar2")

#exercício_03 -------------------------------------------------------------------------------

lista = [0] * 10
for i in range(10):
    lista[i] = int(input(f"Digite o valor {i+1}: "))

qtd_primos = 0

for i in range(10):
    num = lista[i]
    if num > 1:
        eh_primo = True
        for j in range(2, num):
            if num % j == 0:
                eh_primo = False
                break
        if eh_primo:
            qtd_primos += 1

print(f"Quantidade de valores primos: {qtd_primos}")

#exercício_04 -------------------------------------------------------------------------------

tamanho = int(input("Quantidade de elementos: "))

lista1 = [0] * tamanho
lista2 = [0] * tamanho
lista_resultante = [0] * (tamanho * 2)

print("Elementos da Lista 1:")
for i in range(tamanho):
    lista1[i] = input(f"Elemento {i+1}: ")

print("Elementos da Lista 2:")
for i in range(tamanho):
    lista2[i] = input(f"Elemento {i+1}: ")

idx1 = 0
idx2 = 0
for i in range(tamanho * 2):
    if i % 2 == 0:
        lista_resultante[i] = lista1[idx1]
        idx1 += 1
    else:
        lista_resultante[i] = lista2[idx2]
        idx2 += 1

print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"lista3 = {lista_resultante}")

#exercício_05 -------------------------------------------------------------------------------

qtd = int(input("Quantos valores serão fornecidos? "))
lista = [0] * qtd

for i in range(qtd):
    lista[i] = int(input(f"Valor {i+1}: "))

menor = lista[0]
maior = lista[0]
soma = 0

for i in range(qtd):
    if lista[i] < menor:
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
    soma += lista[i]

media = soma / qtd

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Média aritmética: {media}")

#exercício_06 -------------------------------------------------------------------------------

print("Insira os dados em elementos únicos:")
tamanho = int(input("Comprimento da lista/string: "))

lista = [0] * tamanho
for i in range(tamanho):
    lista[i] = int(input(f"Número no índice {i}: "))

texto = input("Digite a string de mesmo comprimento: ")

for i in range(tamanho):
    if i % 2 != 0:
        lista[i] = texto[i]

resultado_str = ""
for i in range(tamanho):
    resultado_str += str(lista[i]) + " "

print(resultado_str)

#exercício_07 -------------------------------------------------------------------------------

qtd = int(input("Quantos valores serão fornecidos? "))
lista = [0] * qtd

for i in range(qtd):
    lista[i] = int(input(f"Valor {i+1}: "))

# 1. ORDENAÇÃO MANUAL
for i in range(qtd):
    for j in range(0, qtd - i - 1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

# 2. CÁLCULO DA MEDIANA
if qtd % 2 != 0:
    mediana = lista[qtd // 2]
else:
    meio1 = lista[(qtd // 2) - 1]
    meio2 = lista[qtd // 2]
    mediana = (meio1 + meio2) / 2

# 3. CÁLCULO DA MODA
frequencia_maxima = 0
moda = "amodal"

for i in range(qtd):
    contagem = 0
    for j in range(qtd):
        if lista[i] == lista[j]:
            contagem += 1
    if contagem > frequencia_maxima:
        frequencia_maxima = contagem
        moda = lista[i]

if frequencia_maxima == 1:
    moda = "amodal"

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")

#exercício_08 -------------------------------------------------------------------------------

tamanho = int(input("Quantos números possui a sua sequência? "))
lista = [0] * tamanho

for i in range(tamanho):
    lista[i] = int(input(f"Digite o número da posição {i}: "))

soma_impares = 0
for i in range(tamanho):
    if i % 2 != 0:
        soma_impares += lista[i]

print(f"Resultado da soma das posições ímpares: {soma_impares}")

#exercício_09 -------------------------------------------------------------------------------

n_palavras = int(input("Quantas palavras vai digitar? "))
palavras = [""] * n_palavras

for i in range(n_palavras):
    palavras[i] = input(f"Palavra {i+1}: ")

palavras_contadas = [""] * n_palavras
ja_contadas_qtd = 0

for i in range(n_palavras):
    palavra_atual = palavras[i]
    
    ja_foi = False
    for k in range(ja_contadas_qtd):
        if palavras_contadas[k] == palavra_atual:
            ja_foi = True
            break
            
    if not ja_foi:
        contador = 0
        for j in range(n_palavras):
            if palavras[j] == palavra_atual:
                contador += 1
        
        print(f"{palavra_atual} = {contador};", end=" ")
        
        palavras_contadas[ja_contadas_qtd] = palavra_atual
        ja_contadas_qtd += 1
print()

#exercício_10 -------------------------------------------------------------------------------

matriz = [[0, 0, 0], [0, 0, 0]]
qtd_impares = 0

for l in range(2):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite o valor para [{l}][{c}]: "))
        if matriz[l][c] % 2 != 0:
            qtd_impares += 1

print("Matriz:")
for l in range(2):
    linha_str = ""
    for c in range(3):
        linha_str += str(matriz[l][c]) + " "
    print(linha_str)

print(f"Quantidade de números ímpares: {qtd_impares}")

#exercício_11 -------------------------------------------------------------------------------

m = int(input("Digite a quantidade de linhas (m): "))
n = int(input("Digite a quantidade de colunas (n): "))

matriz = []
for i in range(m):
    matriz += [[0] * n]

for l in range(m):
    for c in range(n):
        matriz[l][c] = int(input(f"Posição [{l}][{c}]: "))

print(f"Matriz {m} por {n}:")
for l in range(m):
    soma_linha = 0
    linha_str = ""
    for c in range(n):
        linha_str += str(matriz[l][c]) + " "
        soma_linha += matriz[l][c]
    print(f"{linha_str.strip()} = {soma_linha}")

#exercício_12 -------------------------------------------------------------------------------

m = int(input("Digite as linhas (m): "))
n = int(input("Digite as colunas (n): "))

matriz = []
for i in range(m):
    matriz += [[0] * n]

for l in range(m):
    for c in range(n):
        matriz[l][c] = int(input(f"Posição [{l}][{c}]: "))

for l in range(m):
    linha_str = ""
    for c in range(n):
        linha_str += str(matriz[l][c]) + " "
    print(linha_str)

for c in range(n):
    soma_coluna = 0
    for l in range(m):
        soma_coluna += matriz[l][c]
    print(f"Coluna{c+1}: {soma_coluna}")

#exercício_13 -------------------------------------------------------------------------------

matrizA = [[0, 0, 0], [0, 0, 0]]
matrizB = [[0, 0, 0], [0, 0, 0]]
matrizC = [[0, 0, 0], [0, 0, 0]]

print("Preencha a Matriz A:")
for l in range(2):
    for c in range(3):
        matrizA[l][c] = int(input(f"A [{l}][{c}]: "))

print("Preencha a Matriz B:")
for l in range(2):
    for c in range(3):
        matrizB[l][c] = int(input(f"B [{l}][{c}]: "))

# Comparação e montagem de C
for l in range(2):
    for c in range(3):
        if matrizA[l][c] > matrizB[l][c]:
            matrizC[l][c] = matrizA[l][c]
        else:
            matrizC[l][c] = matrizB[l][c]

print("Matriz C (Resultante):")
for l in range(2):
    linha_str = ""
    for c in range(3):
        linha_str += str(matrizC[l][c]) + " "
    print(linha_str)

#exercício_14 -------------------------------------------------------------------------------

matriz = []
for i in range(4):
    matriz += [[0] * 4]

# Leitura da matriz 4x4
for l in range(4):
    for c in range(4):
        matriz[l][c] = int(input(f"Posição [{l}][{c}]: "))

soma = 0

for l in range(4):
    for c in range(4):
        if l % 2 != 0 and c % 2 == 0:
            soma += matriz[l][c]

print(f"Resultado: {soma}")

#exercício_15 -------------------------------------------------------------------------------

import random

m = int(input("Linhas (2 a 10): "))
n = int(input("Colunas (2 a 10): "))

matriz = []
for i in range(m):
    matriz += [[0] * n]

for l in range(m):
    for c in range(n):
        matriz[l][c] = random.randint(100, 999)

for l in range(m):
    linha_str = ""
    for c in range(n):
        linha_str += str(matriz[l][c]) + " "
    print(linha_str)

menor = matriz[0][0]
pos_menor = (0, 0)
maior = matriz[0][0]
pos_maior = (0, 0)

for l in range(m):
    for c in range(n):
        if matriz[l][c] < menor:
            menor = matriz[l][c]
            pos_menor = (l, c)
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            pos_maior = (l, c)

print(f"Menor valor: {menor} na posição {pos_menor}")
print(f"Maior valor: {maior} na posição {pos_maior}")

#exercício_16 -------------------------------------------------------------------------------

import random

matrizA = [[0,0,0], [0,0,0], [0,0,0]]
matrizB = [[0,0,0], [0,0,0], [0,0,0]]
matrizR = [[0,0,0], [0,0,0], [0,0,0]] 


print("Matriz A:")
for l in range(3):
    linha_str = ""
    for c in range(3):
        matrizA[l][c] = random.randint(1, 9)
        linha_str += str(matrizA[l][c]) + " "
    print(linha_str)

print("Matriz B:")
for l in range(3):
    linha_str = ""
    for c in range(3):
        matrizB[l][c] = random.randint(1, 9)
        linha_str += str(matrizB[l][c]) + " "
    print(linha_str)

for l in range(3):
    for c in range(3):
        soma_produto = 0
        for k in range(3):
            soma_produto += matrizA[l][k] * matrizB[k][c]
        matrizR[l][c] = soma_produto

print("Matriz Resultante:")
for l in range(3):
    linha_str = ""
    for c in range(3):
        linha_str += str(matrizR[l][c]) + " "
    print(linha_str)

#exercício_17 -------------------------------------------------------------------------------

import random

j = int(input("Linhas da Matriz A: "))
k_dim = int(input("Colunas da Matriz A: "))
m = int(input("Linhas da Matriz B: "))
n = int(input("Colunas da Matriz B: "))

v_min = int(input("Valor mínimo aleatório: "))
v_max = int(input("Valor máximo aleatório: "))

matrizA = []
for i in range(j):
    matrizA += [[0] * k_dim]

matrizB = []
for i in range(m):
    matrizB += [[0] * n]

for l in range(j):
    for c in range(k_dim):
        matrizA[l][c] = random.randint(v_min, v_max)

for l in range(m):
    for c in range(n):
        matrizB[l][c] = random.randint(v_min, v_max)

print("Matriz A:")
for l in range(j):
    linha_str = ""
    for c in range(k_dim):
        linha_str += str(matrizA[l][c]) + " "
    print(linha_str)

print("Matriz B:")
for l in range(m):
    linha_str = ""
    for c in range(n):
        linha_str += str(matrizB[l][c]) + " "
    print(linha_str)

if k_dim != m:
    print("Impossível realizar o produto matricial (Colunas de A diferente de Linhas de B).")
else:
    matrizR = []
    for i in range(j):
        matrizR += [[0] * n]

    for l in range(j):
        for c in range(n):
            soma = 0
            for x in range(k_dim):
                soma += matrizA[l][x] * matrizB[x][c]
            matrizR[l][c] = soma

    print("Matriz Resultante:")
    for l in range(j):
        linha_str = ""
        for c in range(n):
            linha_str += str(matrizR[l][c]) + " "
        print(linha_str)

#exercício_18 -------------------------------------------------------------------------------

matriz_original = []
matriz_modificada = []
for i in range(3):
    matriz_original += [[0.0] * 6]
    matriz_modificada += [[0.0] * 6]

for l in range(3):
    for c in range(6):
        valor = float(input(f"Posição [{l}][{c}]: "))
        matriz_original[l][c] = valor
        matriz_modificada[l][c] = valor

soma_colunas_impares = 0.0
for l in range(3):
    for c in range(6):
        if c % 2 != 0:
            soma_colunas_impares += matriz_original[l][c]

soma_seg_qua = 0.0
for l in range(3):
    soma_seg_qua += matriz_original[l][1] + matriz_original[l][3]
media_seg_qua = soma_seg_qua / 6 

for l in range(3):
    matriz_modificada[l][5] = matriz_original[l][3] + matriz_original[l][4]

print(f"Soma dos elementos das colunas ímpares: {soma_colunas_impares}")
print(f"Média da segunda e quarta colunas: {media_seg_qua}")

print("\nMatriz Original:")
for l in range(3):
    linha_str = ""
    for c in range(6):
        linha_str += str(matriz_original[l][c]) + " "
    print(linha_str)

print("\nMatriz Modificada:")
for l in range(3):
    linha_str = ""
    for c in range(6):
        linha_str += str(matriz_modificada[l][c]) + " "
    print(linha_str)