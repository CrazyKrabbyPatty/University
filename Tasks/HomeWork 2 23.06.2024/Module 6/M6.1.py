lst = [int(s) for s in input().split()]
lst = [s for s in lst if s%2 != 0]
print(*lst)