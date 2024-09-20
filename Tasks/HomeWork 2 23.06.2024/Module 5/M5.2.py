X = int(input("Введите число X: "))
n = 0
while 2**(n+1) <= X:
    n += 1
print(n, 2**n)