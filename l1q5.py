income = int(input("введите объем выручки "))  # выручка
cost = int(input("введите объем издержек "))  # издержки
# profit = income - cost  # прибыль
profit_ability = (income - cost) / income  # рентабельность
print(income, cost, "+", income - cost, profit_ability)
if income > cost:
    print("поздравляю! вы получили прибыль")
    print("рентабельность = ", profit_ability)
    ppls = int(input("сколько у Вас сотрудников? "))
    print("на одного сотрудника приходится ", (income - cost)/ppls, "единиц прибыли")


