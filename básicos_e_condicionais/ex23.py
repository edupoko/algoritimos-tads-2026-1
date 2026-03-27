# categoria do nadador pela sua idade

idade = int(input("Digite sua idade: "))

match idade:
    case i if i >= 5 and i <= 7:
        print(f"{i} Categoria Infantil")
    case i if i >= 8 and i <= 10:
        print(f"{i} Categoria Juvenil")
    case i if i >= 11 and i <= 15:
        print(f"{i} Categoria Adolescente")
    case i if i >= 16 and i <= 30:
        print(f"{i} Categoria Adulto")
    case i if i > 30:
        print(f"{i} Categoria Sênior")
    case _:
        print("Abaixo do permitido")

# somente if  if

if idade >= 5 and idade <= 7:
    print(f"{idade} Categoria Infantil")
elif idade >= 8 and idade <= 10:
    print(f"{idade} Categoria Juvenil")
elif idade >= 11 and idade <= 15:
    print(f"{idade} Categoria Adolescente")
elif idade >= 16 and idade <= 30:
    print(f"{idade} Categoria Adulto")
elif idade > 30:
    print(f"{idade} Categoria Sênior")


