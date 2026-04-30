def check_par_impar(num: int):

    if not isinstance(num, int):
        print("Somente números inteiros")
        return

    if num % 2 == 0: 
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")

check_par_impar(2)