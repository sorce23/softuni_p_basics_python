quantity_nylon = int(input())
quantity_paint = int(input())
quantity_solvent = int(input())
man_hours = int(input())
price_nylon = 1.50
price_paint = 14.50
price_solvent = 5.00
sacs = 0.40
price_materials = (quantity_nylon + 2) * price_nylon + \
                  (quantity_paint + quantity_paint * 0.1) * price_paint + \
    quantity_solvent * price_solvent + sacs
price_labor = (price_materials * 0.3) * man_hours
total_sum = price_materials + price_labor
print(total_sum)
