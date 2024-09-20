num1 = int(input())
num2 = num1
k = 1
m = 0
while num1 != 0:
    num2 = num1
    num1 = int(input())
    if num2 == num1:
        k += 1
    else:
        if m <= k:
            m = k
        k = 1
print(m)
    
