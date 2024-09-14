month = int(input("Введите номер месяца"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30")
else:
    print("29")