import sys

number = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize
for count in range(1, number + 1):
    current_number = int(input())
    if current_number >= max_num:
        max_num = current_number
    elif current_number <= min_num:
        min_num = current_number
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
