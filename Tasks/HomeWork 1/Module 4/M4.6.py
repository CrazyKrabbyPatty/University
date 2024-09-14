number = int(input("Введите натуральное число: "))
first_number = number // 100
second_number = number // 10 % 10
third_number = number % 10
if first_number < second_number < third_number:
    print("Да")
else:
    print("Нет")
