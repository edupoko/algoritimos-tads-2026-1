#for




# while
i = j = 0

while i <= 10:
    print(f"Iteração {i}")
    i += 1

while i <= 10:
    while j <= 10:
        print(f"Iteração {i} e {j}")
        j += 1
    j = 1
    i += 1

while i <= 10:
    print(i)
    i += 1 
    if i == 4:
        break

while i <= 10:
    i += 1
    if i == 5:
        continue
    print("Iteração", i)

while True:
    opcao = input("Digite uma opção: ")

    match opcao:
        case "":
            print("Comando vazio tente novamente")
            continue
        case "novo":
            print("Novo documento")
        case "salvar":
            print("Documento salvo")
        case "sair":
            break
        case _: #default
            print("Opção inválida")
