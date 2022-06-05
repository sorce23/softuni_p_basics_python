username = input()
password = input()
pass_attempt = input()
while pass_attempt != password:
    pass_attempt = input()
print(f'Welcome {username}!')
