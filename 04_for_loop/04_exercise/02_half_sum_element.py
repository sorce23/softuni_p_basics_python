import sys

number = int(input())
max_num = -sys.maxsize
total_sum = 0
for count in range(1, number + 1):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    total_sum += current_number
if max_num == total_sum - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    sum_others = total_sum - max_num
    print(f'Diff = {abs(max_num - sum_others)}')
