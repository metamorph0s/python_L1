num = int(input("введите целое положительное число "))
b = 0
if num > 0:
    while num != 0:
        a = num % 10
        num = (num - a) / 10
        if b < a:
            b = a
print(b)
