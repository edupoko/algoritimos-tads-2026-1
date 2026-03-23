# imprimindo os dois menores números

num1 = int(input("Digite um num:"))
num2 = int(input("Digite outro num:"))
num3 = int(input("Digite mais outro num:"))

if num1 > num2 and num1 > num3:
    print(num2, num3)
elif num2 > num1 and num2 > num3:
    print(num1, num3)
elif num3 > num1 and num3 > num2:
    print(num1, num2)