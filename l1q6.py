a = int(input("сколько километров Вы пробежали в первый день? "))
b = int(input("сколько километров Вы хотите бегать в день?  "))
c = 1
while a < b:
    a = a * 1.1
    c += 1


print(c)