# imprimindo o menor de 4 num com duas varíaveis

menor = int(input("Digite o primeiro num:"))

num = int(input("Digite o segundo num: "))
if num < menor:
    menor = num

num = int(input("Digite o segundo num: "))
if num < menor:
    menor = num

num = int(input("Digite o segundo num: "))
if num < menor:
    menor = num

print(f"o menor número digitado foi: {menor}")
