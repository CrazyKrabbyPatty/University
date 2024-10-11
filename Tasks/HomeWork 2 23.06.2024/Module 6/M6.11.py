string = input()

first_index = string.lower().index("h")
last_index = string.lower().rindex("h")

print(string[0:first_index + 1] + string[first_index:last_index][::-1] + string[last_index + 1 : len(string)])