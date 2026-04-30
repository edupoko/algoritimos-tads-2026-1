def ordem_crescente(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    print(f"Ordem crescente {a, b, c}")

ordem_crescente(15, 1, 14)