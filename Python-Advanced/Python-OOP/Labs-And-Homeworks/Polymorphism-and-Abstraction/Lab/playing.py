def start_playing(obj):
    return obj.play()


# test code 1
class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))


# test code 2
class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))
