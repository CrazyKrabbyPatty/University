number = int(input("Введите число: "))
if (number % 10 * 1000 + number % 100 // 10 * 100 + number // 100 % 10 * 10 + number // 1000 - number) == 0:
    print("Да")
else:
    print("Нет")