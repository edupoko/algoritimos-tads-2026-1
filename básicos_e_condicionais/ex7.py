# Condicionais
num1 = int(input("Digite um número"))
num2 = int(input("Digite outro número"))

if num1 > num2:
    print(f"O menor é {num2}")
elif num1 == num2 or num2 == num1:
    print("Os valores são iguais")
else:
    print(f"O menor é {num1}")