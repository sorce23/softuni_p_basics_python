film_budget = float(input())
number_people = int(input())
price_costume = float(input())
decorations = film_budget * 0.1
if number_people > 150:
    price_costume *= 0.9
total_expenses = number_people * price_costume + decorations
difference = abs(film_budget - total_expenses)
if total_expenses > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
