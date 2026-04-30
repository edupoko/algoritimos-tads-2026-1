saldo_atual = 0

def depositar(saldo):
    s_deposito = float(input("\nDigite o valor que quer depositar: "))

    while s_deposito <= 0:
        print("\nDepósito inválido")
        s_deposito = float(input("\nDigite o valor que quer depositar: "))

    saldo += s_deposito

    return saldo

def sacar(saldo):
    if saldo <= 0:
        print(f"\n Saldo insuficiente para saque | Saldo: {saldo}")
        return
    else:
        s_sacar = float(input("\nDigite o valor que deseja sacar: "))

    while s_sacar >= saldo:
        print("" \
        "\nSaque inválido")
        s_sacar = float(input("\nDigite o valor que deseja sacar: "))
    else:
        saldo -= s_sacar
    
    return saldo

def menu():

    while True:
        global saldo_atual
        print("\n===Menu===")
        print("1. Ver Saldo")   
        print("2. Depositar")   
        print("3. Sacar")   
        print("0. Sair")

        opcao = input("Digite uma opção: ")

        match opcao:
            case "1":
                print(f"\nSaldo atual: {saldo_atual}")
            case "2":
                saldo_atual = depositar(saldo_atual)
            case "3":
                saldo_atual = sacar(saldo_atual)
            case "0":
                break
            case _:
                print("Opção inválida")

menu()
