total = 0
nota = float(input("Digite uma nota: "))
total += nota

nota = float(input("Digite uma nota: "))
total += nota

nota = float(input("Digite uma nota: "))
total += nota

media = total / 3

print(media)
if media >= 7:
    print(f"Média ponderada: {media:.2f} Aprovado")
elif media >= 3 and media < 7:
    nota_necessaira = 10 - media
    print(f"Média ponderada: {media:.2f} Recuperação")
    print(f"Você precisa tirar: {nota_necessaira:.2f}")
else:
    print(f"Reprovado")
