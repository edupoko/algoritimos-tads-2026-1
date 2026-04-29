#fatorial:
num = 5
fat = 1
for i in range(1, num + 1):
    print(fat, i, fat * i)
    fat *= i

print(fat)