letter_1 = input()
letter_2 = input()
letter_3 = input()
letter_1_ascii = ord(letter_1)
letter_2_ascii = ord(letter_2)
letter_3_ascii = ord(letter_3)
combination_counter = 0
for first_letter in range(letter_1_ascii, letter_2_ascii + 1):
    for second_letter in range(letter_1_ascii, letter_2_ascii + 1):
        for third_letter in range(letter_1_ascii, letter_2_ascii + 1):
            if first_letter != letter_3_ascii and second_letter != letter_3_ascii and third_letter != letter_3_ascii:
                combination_counter += 1
                print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=" ")
print(combination_counter)
