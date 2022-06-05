actor_name = input()
academy_points = float(input())
jury = int(input())
for count in range(jury):
    jury_name = input()
    jury_points = float(input())
    academy_points += (len(jury_name) * jury_points) / 2
    if academy_points > 1250.5:
        break
if academy_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    difference = abs(1250.5 - academy_points)
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')
