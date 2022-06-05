number = int(input())
average_sum = 0
for count in range(number):
    current_number = int(input())
    average_sum += current_number
average_sum = average_sum / number
print(f'{average_sum:.2f}')
