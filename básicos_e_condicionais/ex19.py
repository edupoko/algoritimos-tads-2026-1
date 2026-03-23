total = 0
nota = float(input("Digite uma nota: "))
total += nota

nota = float(input("Digite uma nota: "))
total += nota

nota = float(input("Digite uma nota: "))
total += nota

media = total / 3

print(media)
if media >= 8:
    print(f"Média ponderada: {media:.2f} Conceito: A")
elif media >= 7 and media < 8:
    print(f"Média ponderada: {media:.2f} Conceito: B")
elif media >= 6 and media < 7:
    print(f"Média ponderada: {media:.2f} Conceito: C")
elif media >= 5 and media < 6:
    print(f"Média ponderada: {media:.2f} Conceito: D")
elif media >= 0 and media < 5:
    print(f"Média ponderada: {media:.2f} Conceito: E")
