numero = int(input("Digite um número: "))

match numero:
    case n if n < 100:
        print("Menor que 100")
    case n if n % 2 == 0:
        print(f"{n} é um num positivo par")
    case n:
        print(f"{n} é um num positivo impar")