def cookbook(*args):
    cuisine_recipes = {}

    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cuisine_recipes:
            cuisine_recipes[cuisine] = []
        cuisine_recipes[cuisine].append((recipe_name, ingredients))

    sorted_cuisines = sorted(cuisine_recipes.keys(), key=lambda x: (-len(cuisine_recipes[x]), x))

    result = ''

    for cuisine in sorted_cuisines:
        result += f'{cuisine} cuisine contains {len(cuisine_recipes[cuisine])} recipes:\n'

        sorted_recipes = sorted(cuisine_recipes[cuisine], key=lambda x: x[0])

        for recipe_name, ingredients in sorted_recipes:
            result += f'* {recipe_name} -> Ingredients: {", ".join(ingredients)}\n'

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
