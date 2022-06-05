input_line = input()
total_amount = 0
while input_line != 'NoMoreMoney':
    amount = float(input_line)
    if amount < 0:
        print('Invalid operation!')
        break
    total_amount += amount
    print(f'Increase: {amount:.2f}')
    input_line = input()
print(f'Total: {total_amount:.2f}')
