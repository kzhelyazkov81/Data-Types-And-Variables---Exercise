number_of_snowballs = int(input())
best_snowball_value = 0
best_snowball = ''

for snowball in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball = f'{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})'

print(best_snowball)
