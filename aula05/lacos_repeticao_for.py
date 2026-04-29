for i in range (10):
    print(i)

for i in range (0, 10):
    print(i)

for i in range (0, 10, 2):
    print(i)

for _ in range(10):
    print(i)

# for aninhado
for i in range(11):
    for y in range(11):
        print(f"{i} x {y} = {i * y}")

# else

for i in range(10):
    print(i)
else:
    print("Fim")

# break
for i in range(10):
    print(i)
    if i == 4:
        break

# continue
for i in range(10):
    print(i)
    if i == 5:
        continue
    print("Iteração", i)

        
