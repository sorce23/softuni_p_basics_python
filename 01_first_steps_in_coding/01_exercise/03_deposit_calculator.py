deposit = float(input())
duration = int(input())
annual_interest_percent = float(input())
total_sum = deposit + duration * ((deposit * annual_interest_percent / 100) / 12)
print(total_sum)
