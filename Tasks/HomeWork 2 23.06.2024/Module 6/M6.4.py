a = [int(x) for x in input().split()]

min_index = a.index(min(a))
max_index = a.index(max(a))

temp = a[min_index]
a[min_index] = a[max_index]
a[max_index] = temp

print(*a)