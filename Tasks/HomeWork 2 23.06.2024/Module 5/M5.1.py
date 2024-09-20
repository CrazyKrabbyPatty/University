number = int(input("Введите число >= 2: "))
n = 2
if number % n == 0:
    print(f'Наименьший целочисленный делитель: {n}')
else:
    while number % n != 0:
        n += 1
        if number % n == 0:
            print(f'Наименьший целочисленный делитель: {n}')
            break