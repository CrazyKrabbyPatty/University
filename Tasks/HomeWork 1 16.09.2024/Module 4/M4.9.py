num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите тертье число: "))

if num1 == num2 == num3:
    print("3")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("2")
else:
    print("0")