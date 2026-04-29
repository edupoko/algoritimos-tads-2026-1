'''
1. Crie um programa que exiba um menu interativo para o usuário com
opções de conversão de medidas.
O programa deve rodar continuamente até que o usuário escolha a
opção de sair.
O menu deve ter 3 opções: Converter Celsius para Fahrenheit,
Converter Metros para Centímetros e Sair.
Crie uma função específica para cada cálculo de conversão.
Se o usuário digitar uma opção que não existe, o programa deve
avisar que a opção é inválida e mostrar o menu novamente.
'''

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