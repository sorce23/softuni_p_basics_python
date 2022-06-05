pool_capacity = int(input())
pipe_1_debit = int(input())
pipe_2_debit = int(input())
hours = float(input())
pipe_1 = hours * pipe_1_debit
pipe_2 = hours * pipe_2_debit
total_pipes = pipe_1 + pipe_2
pool_condition = abs(pool_capacity - total_pipes)
percent = (total_pipes / pool_capacity) * 100
percent_pipe_1 = (pipe_1 / total_pipes) * 100
percent_pipe_2 = (pipe_2 / total_pipes) * 100
if total_pipes <= pool_capacity:
    print(f'The pool is {percent:.2f}% full. Pipe 1: {percent_pipe_1:.2f}%. Pipe 2: {percent_pipe_2:.2f}%.')
else:
    print(f'For {hours:.2f} hours the pool overflows with {pool_condition:.2f} liters.')
