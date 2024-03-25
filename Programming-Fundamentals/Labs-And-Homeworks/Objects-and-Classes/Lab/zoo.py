class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        string_for_print = ""
        if species == "mammal":
            string_for_print += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            string_for_print += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            string_for_print += f"Birds in {self.name}: {', '.join(self.birds)}"
        string_for_print += f"\nTotal animals: {Zoo.__animals}"
        return string_for_print


zoo_name = input()
zoo_object = Zoo(zoo_name)
count_of_animals = int(input())
for animals in range(count_of_animals):
    species, name = input().split()
    zoo_object.add_animal(species, name)
searched_species = input()
print(zoo_object.get_info(searched_species))