#1. Faça uma função que não receba parâmetros e escreva na tela (print) o texto “OI”.
def print_oi():
    print("Oi")

print_oi()

#2. Faça uma função que receba um texto por parâmetro e escreva-o na tela (print).
def receber_texto(texto):
    print(texto)

receber_texto("Pera")

#3. Faça uma função que receba um texto por parâmetro e escreva-o na tela (print), em seguida retorne “Ok”
def receber_texto_ok(texto):
    print(texto)
    return "Ok"

print(receber_texto_ok("Abacate"))

#4. Faça um procedimento que recebe por parâmetro os valores necessários para ocálculo da fórmula de báskara e imprima as suas raízes, caso seja possível calcular
def baskahra(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0: return None

    bask1 = (-b + delta ** 0.5) / (2 * a)
    bask2 = (-b - delta ** 0.5) / (2 * a)

    return (bask1, bask2)

print(baskahra(1, -5, 6))

#5. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito,6 = 1 + 2 + 3, que são seus divisores).
def valor_perfeito(num):
    soma = 0

    for i in range(1, num):
        if num % i == 0:
            soma += i

    if soma == num:
        print("Num perfeito")
    else:
        print("Não é perfeito")

valor_perfeito(496)


