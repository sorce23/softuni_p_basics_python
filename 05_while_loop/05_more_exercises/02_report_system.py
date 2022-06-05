final_sum = int(input())
counter = 0
payment_by_card = 0
payment_in_cash = 0
card_counter = 0
cash_counter = 0
total_sum = 0
is_failed = False
while final_sum > total_sum:
    command = input()
    if command == 'End':
        is_failed = True
        break
    counter += 1
    payment = int(command)
    if counter % 2 != 0:
        if payment > 100:
            print('Error in transaction!')
            continue
        else:
            payment_in_cash += payment
            cash_counter += 1
            print('Product sold!')
    elif counter % 2 == 0:
        if payment < 10:
            print('Error in transaction!')
            continue
        else:
            payment_by_card += payment
            card_counter += 1
            print('Product sold!')
    total_sum += payment
if is_failed:
    print('Failed to collect required money for charity.')
else:
    average_cash = payment_in_cash / cash_counter
    average_card = payment_by_card / card_counter
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')
