turns = int(input())
game_9 = 0
game_19 = 0
game_29 = 0
game_39 = 0
game_50 = 0
invalid = 0
final_result = 0
for count in range(turns):
    dice = int(input())
    if 0 <= dice <= 9:
        final_result += dice * 0.2
        game_9 += 1
    elif 10 <= dice <= 19:
        final_result += dice * 0.3
        game_19 += 1
    elif 20 <= dice <= 29:
        final_result += dice * 0.4
        game_29 += 1
    elif 30 <= dice <= 39:
        final_result += 50
        game_39 += 1
    elif 40 <= dice <= 50:
        final_result += 100
        game_50 += 1
    else:
        final_result = final_result / 2
        invalid += 1
game_9 = game_9 / turns * 100
game_19 = game_19 / turns * 100
game_29 = game_29 / turns * 100
game_39 = game_39 / turns * 100
game_50 = game_50 / turns * 100
invalid = invalid / turns * 100
print(f'{final_result:.2f}')
print(f'From 0 to 9: {game_9:.2f}%')
print(f'From 10 to 19: {game_19:.2f}%')
print(f'From 20 to 29: {game_29:.2f}%')
print(f'From 30 to 39: {game_39:.2f}%')
print(f'From 40 to 50: {game_50:.2f}%')
print(f'Invalid numbers: {invalid:.2f}%')
