a = 'hello' #string
b = 4 #int
c = 4.5 #float 
d = True or False #boolean

# caracter de escape \n
print("Olá mundo!\npula uma linha")

# indicando tipo de dado para guardar
nome: str = "Eduardo"
idade: int = 35

# f-string  
print(f'Olá {nome}. Vc tem {idade} anos')

# sem f-string concatenaçâo
print('Olá, ' + nome + '. Vc tem' + str(idade) + 'anos')

# virgulas no print
print('Olá, ', nome, 'Vc tem', idade, 'anos')

print("Olá, {}. VC tem {} anos".format(nome, idade))

preco = 10 
quantidade = 3

print(f"O total da compra é: {10 * quantidade}")