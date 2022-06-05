import math

tournaments = int(input())
ranklist_points = int(input())
tournament_points = 0
wins = 0
for count in range(tournaments):
    stage = input()
    if stage == 'W':
        tournament_points += 2000
        wins += 1
    elif stage == 'F':
        tournament_points += 1200
    elif stage == 'SF':
        tournament_points += 720
final_points = ranklist_points + tournament_points
average_points = tournament_points / tournaments
percentage_of_wins = (wins / tournaments) * 100
print(f'Final points: {final_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{percentage_of_wins:.2f}%')
