class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        raise StopIteration


# test code
one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)