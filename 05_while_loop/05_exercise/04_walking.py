target_steps = 10000
total_steps = 0
is_going = False
while total_steps < target_steps:
    command = input()
    if command == 'Going home':
        last_steps = int(input())
        total_steps += last_steps
        is_going = True
        break
    current_steps = int(command)
    total_steps += current_steps
difference = abs(target_steps - total_steps)
if is_going:
    print(f'{difference} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
