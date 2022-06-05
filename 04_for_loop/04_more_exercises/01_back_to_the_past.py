money = float(input())
year = int(input())
total_sum = 0
age = 18
for count in range(1800, year + 1):
    if count % 2 == 0:
        total_sum += 12000
        age += 1
    else:
        total_sum += 12000 + age * 50
        age += 1
difference = abs(money - total_sum)
if total_sum <= money:
    print(f'Yes! He will live a carefree life and will have {difference:.2f} dollars left.')
else:
    print(f'He will need {difference:.2f} dollars to survive.')
