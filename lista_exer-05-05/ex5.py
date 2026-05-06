def soma_inderteminavel(n, s, c):
    s += n 
    c += 1

    m = s / c

    return m, s, c

soma = 0
contador = 0

while True:
    num = int(input("Digite um numero ou 0 para parar: "))

    if num < 0:
        print("Número inválido, negativo")
    elif num == 0:
        break
    else:
        media, soma, contador = soma_inderteminavel(num, soma, contador)
        print(f"Média: {media} | Soma: {soma}")