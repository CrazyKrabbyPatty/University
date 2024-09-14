print("Введите часы, минуты, секунды в соответствующем порядке для первой метки")
h1 = int(input())
m1 = int(input())
s1 = int(input())

print("Введите часы, минуты, секунды в соответствующем порядке для второй метки")
h2 = int(input())
m2 = int(input())
s2 = int(input())

AllSeconds1 = h1*60**2 + m1*60 + s1
AllSeconds2 = h2*60**2 + m2*60 + s2

print("Разница между двумя метками = ", (AllSeconds2 - AllSeconds1))