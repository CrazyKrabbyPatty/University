import random

print("Отгадай число!")

hidden_number = random.randint(0, 100)
print("Компьютер загадал число: ", hidden_number)

count = 0

while True:
    user_input = input("Ввод пользователя: ")

    if user_input == "Выход":
        print("Вы забуксовали")
        break
    
    count += 1

    if int(user_input) < hidden_number:
        print("Ваше число меньше!")
    elif  int(user_input) > hidden_number:
        print("Ваше число больше!")
    else:
        print("Поздравляем! Вы мэрлин, ведь вы угадали число за " + str(count) + " попытки!")
        break