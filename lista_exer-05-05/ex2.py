votou = 0
n_voto = 0
cont = 0
pessoas = int(input("Digite quantas pessoas vão ser verificadas: "))


while cont <= pessoas:
    idade = int(input("Digite sua idade: "))
    cont += 1

    if idade >= 16 and idade <= 17 or idade >= 65:

        voto = input("Digite [s] se vc votou ou [n] se não votou: ")

        match voto:
            case "s":
                votou += 1
            case "n":
                n_voto += 1
            case "_":
                print("Opção inválida")

    elif idade >= 18 and idade < 65:
        votou += 1
        print("Votou obrigatoriamente")
    else:
        print("Não pode votar")

print(f"Votaram: {votou} | Nâo votaram {n_voto}")