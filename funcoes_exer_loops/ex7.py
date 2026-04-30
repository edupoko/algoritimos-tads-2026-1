def pedir_nums():
    lista = []

    while True:
        try:
            entrada = (input("Digite um número ou sair: "))

            if entrada == 'sair':
                break

            num = float(entrada)
            lista.append(num)

        except ValueError:
            print("Digite somente numeors válidos")
    
    if lista:
        print(f"Média: {sum(lista) / len(lista):.2f}")
        print(f"Menor: {min(lista)}")
        print(f"Maior: {max(lista)}")
    else:
        print("Nenhum número digitado")

pedir_nums()