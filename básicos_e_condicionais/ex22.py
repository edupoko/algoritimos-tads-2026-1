# verifica se é triângulo e o tipo

a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a < b + c or b < a + c or c < a + b:
    print("É um triângugulo")
    
    if a == b and a == c:
        print("Tipo: Equilátero, todos lados iguais")
    elif a == b or b == c or a == c:
        print("Tipo: Isósceles, dois lados iguais")
    elif a != b and a != c and b != c:
        print("Tipo: Escaleno, todos os lados diferentes")

else:
    print("Não é triângulo")