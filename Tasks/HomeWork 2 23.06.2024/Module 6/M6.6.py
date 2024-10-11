lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

a = set()

for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == lst2[j]: a.add(lst1[i])

print(*sorted(a))