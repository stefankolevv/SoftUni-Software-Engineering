def logged(func):
    def wrapper(*args, **kwargs):
        return f"you called {func.__name__}{args}\n" \
               f"it returned {func(*args, **kwargs)}"

    return wrapper

@logged
def sum_numbers(a, b):
    return a + b


print(sum_numbers(5, 4))