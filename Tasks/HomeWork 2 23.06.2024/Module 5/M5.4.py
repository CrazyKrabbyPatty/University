n = int(input())
m = 0
k = 0
while n != 0:
    m = n
    n = int(input())
    if m < n:
        k += 1
print(k)