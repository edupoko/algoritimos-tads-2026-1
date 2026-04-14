soma_maiores = 0
soma_menores = 0
pessoas = 1
contador = 0

while True:
    idade = input(f"Digite a idade da pessoa {pessoas}: ")
    pessoas += 1

    if idade == "":
        break

    converter = int(idade)

    if converter >= 18:
        soma_maiores += converter
    elif converter < 18:
        contador += 1
        soma_menores += converter

print(f"Soma dos maiores {soma_maiores}")
print(f" Média {(soma_menores/ contador):.2f}")
