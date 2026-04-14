soma = 0

while True:
    num = input("Digite um num ou enter para finalizar: ")

    if num == '':
        break
    else:
        conversor = float(num)
    soma += conversor

print(soma)