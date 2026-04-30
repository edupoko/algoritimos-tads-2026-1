def verificarSinal(num: int):

    if not isinstance(num, int):
        print("Somente números inteiros")
        return

    if num > 0: 
        print(f"{num} é positivo")
    elif num < 0:
        print(f"{num} é negativo")
    else:
        print("Nulo")

verificarSinal(8)