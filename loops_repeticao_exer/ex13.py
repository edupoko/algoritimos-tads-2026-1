lista = []

for i in range(5):
    num = int(input("Digite um num: "))
    lista.append(num)
    

print(sorted(lista))
print(sorted(lista, reverse=True))
