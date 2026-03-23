# menor de três números
num1 = 7
num2 = 9
num3 = 10

if num1 < num2 and num1 < num3:
    print(f"O menor é {num1}")
elif num2 < num1 and num2 < num3:
    print(f"O menor é {num2}")
elif num3 < num1 and num3 < num2:
    print(f"O menor é {num3}")
elif num1 and num2 and num3 == num1:
    print("Os valores são iguais")
else:
    print("Valor inválido")