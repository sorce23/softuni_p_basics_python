length_of_room = int(input())
width_of_room = int(input())
height_of_room = int(input())
free_space = length_of_room * width_of_room * height_of_room
room_is_free = True
command = input()
while command != 'Done':
    number_of_boxes = int(command)
    free_space -= number_of_boxes
    if free_space < 0:
        room_is_free = False
        break
    command = input()
if room_is_free:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
