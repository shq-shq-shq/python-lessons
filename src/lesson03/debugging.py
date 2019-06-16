x = 7

def isDivisibleBy(x, i):
    return x % i == 0

for i in range(2, x):
    print("Проверяем делимость на ", i)
    if isDivisibleBy(x, i):
        print("Число делится")
    else:
        print("Число не делится")

print("Цикл выполнился полностью")

