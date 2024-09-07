
#Exercício do desafio do bootcamp DIO + NTTDATA

#Criando um sistema bancário com Python

menu = """
[1]- Depositar
[2]- Sacar
[3]- Extrato
[4]- Sair
"""

extrato = []
saldo = 0
limite_saque = 500
saques_realizados = 0
LIMITE_SAQUE = 3


def depositar(valor):
    global saldo
    if valor > 500:
        print("O valor máximo para depósito é de R$500.")
        return
    saldo += valor
    extrato.append(f"+ R$ {valor:.2f}")
    print(f"Você depositou R$ {valor:.2f} com sucesso!")


def sacar(valor):
    global saldo
    global saques_realizados
    if saques_realizados >= LIMITE_SAQUE:
        print("Limite de saque diário excedido.")
        return
    if valor > limite_saque:
        print(f"O valor máximo para saque é de R$ {limite_saque:.2f}.")
        return
    if saldo >= valor:
        saldo -= valor
        extrato.append(f"-R$ {valor:.2f}")
        saques_realizados += 1
        print(f"Você sacou R$ {valor:.2f} com sucesso!")
    else:
        print("Saldo insuficiente.")


def exibir_extrato():
    print("\nExtrato:")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}\n")


while True:
    comando = input(f"Escolha uma opção: {menu}")

    if comando == "1":
        try:
            valor = float(input("Quanto deseja depositar? "))
            depositar(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

    elif comando == "2":
        try:
            valor = float(input("Quanto deseja sacar? "))
            sacar(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

    elif comando == "3":
        exibir_extrato()

    elif comando == "4":
        print("Obrigado por usar nosso banco. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
