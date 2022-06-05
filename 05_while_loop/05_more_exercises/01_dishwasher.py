bottles_of_detergent = int(input())
command = input()
dishes = 0
pots = 0
detergent = bottles_of_detergent * 750
counter = 0
detergent_is_enough = True
while command != 'End':
    current_number = int(command)
    counter += 1
    if counter % 3 == 0:
        pots += current_number
        detergent -= current_number * 15
    else:
        dishes += current_number
        detergent -= current_number * 5
    if detergent < 0:
        detergent_is_enough = False
        break
    command = input()
if detergent_is_enough:
    print('Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
else:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
