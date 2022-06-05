total_tickets = 0
student_tickets = 0
kid_tickets = 0
standard_tickets = 0
command = input()
while command != 'Finish':
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places = free_places
    while free_places > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
        free_places -= 1
        sold_tickets += 1
        total_tickets += 1
    percent_capacity = sold_tickets / total_places * 100
    print(f'{movie_name} - {percent_capacity:.2f}% full.')
    command = input()
students_percent = student_tickets / total_tickets * 100
standard_percent = standard_tickets / total_tickets * 100
kid_percent = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f'{students_percent:.2f}% student tickets.')
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
