import os 
import platform
from time import sleep

def limpa_tela():
    if platform.system == "windows":
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print("------- Bem vindos ao AriBank --------")
    print("Saque [1]")
    print("Depósito [2]")
    print("Extrato [3]")
    print("Sair [0]")
        

saldo = 0
valor = 0
extrato = 0
move = 0

while True:
    limpa_tela()
    menu() 
    
    opc = int(input("Qual a sua opção? "))
    
    if opc == 1:
        valor = float(input("Quanto deseja sacar? "))
        if valor < 0:
            print("Você não possui saldo suficiente para saque, adicione dinheiro para continuar!")
            sleep(5)
            saldo == 0
        saldo -= valor
        move += 1
        print(f"Seu saldo é: {saldo}")
    elif opc == 2:
        valor = float(input("Quanto deseja depositar? "))
        saldo += valor
        move += 1
    elif opc == 3:
        print("---- EXTRATO ----")
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
        print(f"Foram feitas {move} movimentações na sua conta")
        sleep(5)
    elif opc == 0:
        print("Obrigado por usar nosso banco, até mais")
        break