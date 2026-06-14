#exercício_01 -------------------------------------------------------------------------------

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
estado = input("Digite o estado: ")

dados = (nome, idade, estado)

print(f"Nome: {dados[0]}")
print(f"Idade: {dados[1]}")
print(f"Estado: {dados[2]}")

#exercício_02 -------------------------------------------------------------------------------

x1 = int(input("Ponto 1 (x): "))
y1 = int(input("Ponto 1 (y): "))
x2 = int(input("Ponto 2 (x): "))
y2 = int(input("Ponto 2 (y): "))

ponto1 = (x1, y1)
ponto2 = (x2, y2)

px1, py1 = ponto1
px2, py2 = ponto2

distancia = (((px2 - px1) ** 2) + ((py2 - py1) ** 2)) ** 0.5

print(f"Distância: {distancia:.2f}")

#exercício_03 -------------------------------------------------------------------------------

print("Informe 3 frutas:")
f1 = input("Fruta 1: ")
f2 = input("Fruta 2: ")
f3 = input("Fruta 3: ")
tupla_frutas = (f1, f2, f3)

print("Informe 2 vegetais:")
v1 = input("Vegetal 1: ")
v2 = input("Vegetal 2: ")
tupla_vegetais = (v1, v2)

tupla_alimentos = tupla_frutas + tupla_vegetais

print("Alimentos:")
print(tupla_alimentos)

#exercício_04 -------------------------------------------------------------------------------

# Criação da lista de números inicial
lista = [1, 2, 3, 4, 5]

# Conversão explícita para tupla
tupla_original = tuple(lista)

# Uso de fatiamento (slice) para pegar os 3 primeiros elementos (índices 0, 1 e 2)
tupla_fatiada = tupla_original[0:3]

print(f"lista: {lista}")
print(f"Tupla: {tupla_original}")
print(f"Slice da tupla: {tupla_fatiada}")

#exercício_05 -------------------------------------------------------------------------------

tupla_inicial = (1, 2, 3, 4, 5)

pos1 = int(input("Digite a posição 1: "))
pos2 = int(input("Digite a posição 2: "))

# Como tuplas são imutáveis, convertemos para lista para poder alterar [cite: 200]
lista_aux = list(tupla_inicial)

# Realiza a troca das posições usando uma variável auxiliar
aux = lista_aux[pos1]
lista_aux[pos1] = lista_aux[pos2]
lista_aux[pos2] = aux

# Converte de volta para tupla [cite: 200]
tupla_final = tuple(lista_aux)

print(f"Tupla A: {tupla_inicial}")
print(f"Tupla B: {tupla_final}")

#exercício_06 -------------------------------------------------------------------------------

lista_inicial = [1, 1, 2, 3, 3, 4, 4]

conjunto_resultante = set(lista_inicial)

maior_valor = -9999999
for elemento in conjunto_resultante:
    if elemento > maior_valor:
        maior_valor = elemento

dobro_maior = maior_valor * 2
conjunto_resultante.add(dobro_maior)

print(f"Lista: {lista_inicial}")
print(f"Conj: {conjunto_resultante}")

#exercício_07 -------------------------------------------------------------------------------

conjunto_A = {1, 2, 3, 4}
conjunto_B = {2, 5, 7, 9}
conjunto_C = {1, 4, 7, 6}

resultado_uniao = conjunto_A.union(conjunto_B)
resultado_diferenca = resultado_uniao.difference(conjunto_C)

print(f"União: {resultado_uniao}")
print(f"Diferença: {resultado_diferenca}")

#exercício_08 -------------------------------------------------------------------------------

valores_entrada = [1, 9, 3, 2, 3, 6, 4]
conj1 = set(valores_entrada)

divisor = int(input("Digite o divisor: "))

conj2 = set()

for elemento in conj1:
    if elemento % divisor == 0:
        conj2.add(elemento)

print(f"Divisor: {divisor}")
print(f"Conj 1: {conj1}")
print(f"Conj 2: {conj2}")

#exercício_09 -------------------------------------------------------------------------------

conjunto_A = {1, 'a', 8, '4'}
conjunto_B = {8, '4'}

# Verificação manual se B é subconjunto de A
eh_subconjunto = True
for elemento in conjunto_B:
    if elemento not in conjunto_A:
        eh_subconjunto = False
        break

if eh_subconjunto:
    print("B é subconjunto de A")
else:
    print("B não é subconjunto de A")

# Criação de C contendo elementos de A que não estão em B 
conjunto_C = set()
for elemento in conjunto_A:
    if elemento not in conjunto_B:
        conjunto_C.add(elemento)

print(f"A: {conjunto_A}")
print(f"B: {conjunto_B}")
print(f"C: {conjunto_C}")

#exercício_10 -------------------------------------------------------------------------------

conjunto_dados = set()

print("--- Preenchendo o Conjunto (digite '$$' para parar) ---")
while True:
    entrada = input("Digite um valor para o conjunto: ")
    if entrada == "$$":
        break
    # Força a adição via operador de união in-place '|=' conforme exigido [cite: 221]
    conjunto_dados |= {entrada}

lista_valores = []
print("\n--- Preenchendo a Lista (digite '$$' para parar) ---")
while True:
    entrada = input("Digite un valor para a lista: ")
    if entrada == "$$":
        break
    lista_valores += [entrada]

# Criação manual do texto de saída analisando as presenças
resultado_analise = ""
for i in range(len(lista_valores)):
    item = lista_valores[i]
    if item in conjunto_dados:
        presenca = "Sim"
    else:
        presenca = "Não"
    
    resultado_analise += f"{item}:{presenca}"
    if i < len(lista_valores) - 1:
        resultado_analise += ", "

print(f"\nConjunto: {conjunto_dados}")
print(f"Lista: {resultado_analise}")

#exercício_11 -------------------------------------------------------------------------------

frase = input("Digite o texto: ")

frase_limpa = ""
for caractere in frase:
    if caractere != "." and caractere != ",":
        frase_limpa += caractere

palavras = []
palavra_atual = ""
for caractere in frase_limpa:
    if caractere == " ":
        if palavra_atual != "":
            palavras += [palavra_atual]
            palavra_atual = ""
    else:
        palavra_atual += caractere
if palavra_atual != "":
    palavras += [palavra_atual]

dicionario_contagem = {}
for p in palavras:
    if p in dicionario_contagem:
        dicionario_contagem[p] += 1
    else:
        dicionario_contagem[p] = 1

print(f"Contagem de palavras: {dicionario_contagem}")

#exercício_12 -------------------------------------------------------------------------------

lista_itens = [('banana', 3), ('uva', 5), ('uva', 2), ('banana', 2), ('pêra', 2)]

dicionario_frutas = {}

for item in lista_itens:
    fruta = item[0]
    quantidade = item[1]
    
    if fruta in dicionario_frutas:
        dicionario_frutas[fruta] += quantidade
    else:
        dicionario_frutas[fruta] = quantidade

print(f"Lista: {lista_itens}")
print(f"Valores: {dicionario_frutas}")

#exercício_13 -------------------------------------------------------------------------------

aluno_nota = {'Ana': 70, 'José': 80, 'João': 20, 'Rita': 20}

nota_aluno = {}

for aluno in aluno_nota:
    nota = aluno_nota[aluno]
    
    
    if nota not in nota_aluno:
        nota_aluno[nota] = [aluno]
    else:
    
        nota_aluno[nota] += [aluno]


for nota in nota_aluno:
    if len(nota_aluno[nota]) == 1:
        nota_aluno[nota] = nota_aluno[nota][0]

print(f"nota_aluno: {nota_aluno}")

#exercício_14 -------------------------------------------------------------------------------

loja1 = {'Item 1': 10, 'Item 2': 5, 'Item 3': 10}
loja2 = {'Item 1': 10, 'Item 2': 2, 'Item 4': 10}

estoque_total = {}

for item in loja1:
    estoque_total[item] = loja1[item]

for item in loja2:
    if item in estoque_total:
        estoque_total[item] += loja2[item]
    else:
        estoque_total[item] = loja2[item]

print(f"Loja 1: {loja1}")
print(f"Loja 2: {loja2}")
print(f"Estoque: {estoque_total}")

#exercício_15 -------------------------------------------------------------------------------

qtd_vendedores = int(input("Quantidade de vendedores a cadastrar: "))
vendedores = [""] * qtd_vendedores

for i in range(qtd_vendedores):
    vendedores[i] = input(f"Nome do vendedor {i+1}: ")

relatorio_vendas = {}

for vendedora in vendedores:
    print(f"\nColetando dados de: {vendedora}")
    soma_vendas = 0
    for mes in range(3):
        venda_mes = float(input(f"Venda do mês {mes+1}: "))
        soma_vendas += venda_mes
    relatorio_vendas[vendedora] = soma_vendas

lista_tuplas = []
for vendedora in relatorio_vendas:
    lista_tuplas += [(vendedora, relatorio_vendas[vendedora])]

n = len(lista_tuplas)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista_tuplas[j][1] < lista_tuplas[j+1][1]:
            aux = lista_tuplas[j]
            lista_tuplas[j] = lista_tuplas[j+1]
            lista_tuplas[j+1] = aux

print(f"\nDicionário do Relatório: {relatorio_vendas}")
print(f"Lista de Tuplas Ordenada: {lista_tuplas}")