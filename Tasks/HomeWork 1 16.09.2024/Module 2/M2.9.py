minutes = int(input("Введите количество минут, прошедших после полуночи: "))
hours = minutes // 60
print(hours,minutes - hours*60, sep=":")