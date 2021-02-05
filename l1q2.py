all_sec = int(input("сколько всего секунд? "))
sec = all_sec % 60
all_min = all_sec // 60
min = all_min % 60
hour = all_min // 60

print(f'{all_sec} секунд это {hour} часов, {min} минут, {sec} секунд')