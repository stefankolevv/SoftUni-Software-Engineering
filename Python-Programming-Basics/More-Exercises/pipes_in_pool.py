volume = int(input())
first_pipe_flow_rate = int(input())
second_pipe_flow_rate = int(input())
worker_missing_hours = float(input())
overflow = 0

total_filled = (first_pipe_flow_rate + second_pipe_flow_rate) * worker_missing_hours

if total_filled <= volume:
    pool_percentage = (total_filled / volume) * 100
    first_pipe_percentage = (first_pipe_flow_rate * worker_missing_hours / total_filled) * 100
    second_pipe_percentage = (second_pipe_flow_rate * worker_missing_hours / total_filled) * 100
    print(f"The pool is {pool_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.")
else:
    overflow = total_filled - volume
    print(f"In {worker_missing_hours:.2f} hours the pool overflows with {overflow:.2f} liters.")
