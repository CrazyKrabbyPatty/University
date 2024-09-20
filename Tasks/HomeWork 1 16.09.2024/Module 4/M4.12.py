month = int(input("Введите номер месяца: "))
day = int(input("Введите день месяца: "))
year = 2024
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if 1 <= day < 31:
        day += 1
        print(day,month,year, sep='-')
    elif day == 31 and month == 12:
        year += 1
        day = 1
        month = 1
        print(day,month,year, sep='-')
    else:
        month += 1
        day = 1
        print(day,month,year, sep='-')
elif month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day < 30:
        day += 1
        print(day,month,year, sep='-')
    else:
        month += 1
        day = 1
        print(day,month,year, sep='-')
else:
    if 1 <= day < 28:
        day += 1
        print(day,month,year, sep='-')
    else:
        month += 1
        day = 1
        print(day,month,year, sep='-')