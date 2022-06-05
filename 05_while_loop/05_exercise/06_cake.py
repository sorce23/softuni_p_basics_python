cake_length = int(input())
cake_width = int(input())
pieces = cake_width * cake_length
cake_is_finished = False
command = input()
while command != 'STOP':
    current_number = int(command)
    pieces -= current_number
    if pieces < 0:
        cake_is_finished = True
        break
    command = input()
if cake_is_finished:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')
else:
    print(f'{pieces} pieces are left.')
