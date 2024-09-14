number = int(input("Введите трёхзначное число: "))
FirstNumber = number // 100
SecondNumber = number // 10 % 10
ThirdNumber = number % 10
print(FirstNumber+SecondNumber+ThirdNumber)