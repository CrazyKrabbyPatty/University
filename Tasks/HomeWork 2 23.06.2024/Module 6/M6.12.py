string = input()

first_index = string.lower().index("h") + 1
last_index = string.lower().rindex("h") - 1

print(string[0 : first_index] + string[first_index : last_index].replace('h', 'H') + string[last_index : len(string)])
