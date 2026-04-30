import random

def digitar100n():
    soma_positivos = 0
    soma_negativos = 0
    cont = 0
    cont2 = 0

    for _ in range(100):
        num = random.uniform(-100, 100) 

        if num > 0:
            soma_positivos += num
            cont += 1
        elif num < 0:
            soma_negativos += num
            cont2 += 1

    m_pos = soma_positivos / cont if cont > 0 else 0
    m_neg = soma_negativos / cont2 if cont2 > 0 else 0

    print(f"Total Positivos: {cont} | Total Negativos: {cont2}")
    print(f"Média Positivos: {m_pos:.2f} | Média Negativos: {m_neg:.2f}")
    print(f"Diferença das somas: {soma_positivos - soma_negativos:.2f}")

digitar100n()
