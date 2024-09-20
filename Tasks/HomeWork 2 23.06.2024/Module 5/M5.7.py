N = int(input("Введите число N: "))
f0 = 0; f1 = 1; f = 1; i = 2
while i != N:
    f0 = f1
    f1 = f
    f = f0 + f1
    i += 1
if N == i:
    print(f)