line = input("Введите слово: ")
if line.count("f") <= 1:
    print(line.find("f"))
else:
    print(line.find("f"),line.rfind("f"))
