a = [int(x) for x in input().split()]
for i in range(len(a)-1, ):
    a[i] = a[i+1]
print(*a)