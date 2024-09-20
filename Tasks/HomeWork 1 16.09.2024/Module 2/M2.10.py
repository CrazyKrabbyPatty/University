students1 = int(input("Введите количество учеников в первом классе: "))
students2 = int(input("Введите количество учеников во втором классе: "))
students3 = int(input("Введите количество учеников в третьем классе: "))

tables1 = students1 // 2 + students1 % 2
tables2 = students2 // 2 + students2 % 2
tables3 = students3 // 2 + students3 % 2

print("Минимальное количество столов для приобретения = ", tables1+tables2+tables3) 