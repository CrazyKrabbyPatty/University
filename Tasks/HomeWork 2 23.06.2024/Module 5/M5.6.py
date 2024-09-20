N = int(input("Введите число N: "))
f0 = 0; f1 = 1; f = 1; i = 2
if (N >= f):
    while f != N:
        f0 = f1
        f1 = f
        f = f0 + f1
        i += 1
        if N < f:
            break
if N < f:
    print(-1)
else:
    print(i)