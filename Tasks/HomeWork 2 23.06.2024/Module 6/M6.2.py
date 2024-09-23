lst = [int(s) for s in input().split()]
ans = []
for i in range(len(lst)-1):
    if lst[i]<lst[i+1]:
        ans.append(lst[i+1])
print(*ans)