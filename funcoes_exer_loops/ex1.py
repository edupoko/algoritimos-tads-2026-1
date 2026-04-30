def conversor_ctf():
    fah = float(input("\nDigite a temperatura em Fahrenheit: \n"))
    graus = 5 / 9 * (fah - 32)
    print(f"\nA temperatura em graus é: {graus:.2f}\n")
    menu()

def conversor_mtc():
    metros = float(input("\nDigite o valor em metros: \n"))
    centi = metros * 100
    print(f"\nO valor em centimetro é: {centi} cm\n")
    menu()

def menu():

    while True:
        print("=====MENU=====")
        print("1. Converter Celsius para Fahrenheit")
        print("2. Conveter metros para centímetros")
        print("0. Sair")

        opcao = input("Digite o valor da opção: ")

        match opcao:
                case "1":
                    conversor_ctf()
                case "2":
                    conversor_mtc()
                case "0":
                    break
                case _:
                    print("\nOpção inválida\n")

menu()