class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        space_left = Glass.capacity - self.content
        if ml <= space_left:
            self.content += ml
            return f'Glass filled with {ml} ml'
        else:
            return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        space_left = Glass.capacity - self.content
        return f'{space_left} ml left'

# Test code
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
