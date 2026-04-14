lista = []

for i in range(3):
    num = int(input("Digite um num:"))
    lista.append(num)

for i in range(len(lista)):
    if lista[i] > 25:
        print(f"{lista[i]} é maior que 25")
    if lista[i] < 85:
        print(f"{lista[i]} é menor que 85")
    