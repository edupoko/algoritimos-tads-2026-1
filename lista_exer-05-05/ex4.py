def cat_nadador(idade):
    if idade >= 4 and idade <= 6:
        return "Categoria: Infantil A"
    elif idade >= 7 and idade <= 9:
        return "Categoria: Infantil B"
    elif idade >= 10 and idade <= 14:
        return "Categoria: Juvenil A"
    elif idade >= 15 and idade <= 17:
        return "Categoria: Juvenil B"
    elif idade >= 18:
        return "Categoria: Adulto"
    else:
        return "Perigoso"

i = int(input("Digite sua idade: "))

categoria = cat_nadador(i)
print(categoria)