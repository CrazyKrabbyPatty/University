lst = [x for x in input().split()]
repeatable_value = set()
for i in range(0, len(lst)):
    if lst[i] in repeatable_value:
        print("ДА")
    else:
        print("НЕТ")
        repeatable_value.add(lst[i])