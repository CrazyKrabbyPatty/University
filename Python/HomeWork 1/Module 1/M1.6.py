N = int(input("Введите количество секунд, прошедших после полуночи "))
minutes = N // 60
hours = minutes // 60
print(str(hours) + " полный час после полуночи, " + str(minutes) + " полных минут после полуночи")