number = int(input())
points = 0
if number <= 100:
    points += 5
elif number < 1000:
    points += number * 0.2
elif number > 1000:
    points += number * 0.1
if number % 2 == 0:
    points += 1
if number % 10 == 5:
    points += 2
total = points + number
print(f'{points}')
print(f'{total}')
