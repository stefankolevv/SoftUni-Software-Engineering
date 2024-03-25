percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_num_calories = int(input())
percent_containing_water = int(input())

total_gr_fats = (percent_fats * total_num_calories) / 9
total_gr_proteins = (percent_proteins * total_num_calories) / 4
total_gr_carbohydrates = (percent_carbohydrates * total_num_calories) / 4

weight_food = total_gr_fats + total_gr_proteins + total_gr_carbohydrates
calories_one_gr_food = total_num_calories / weight_food
percent_food = 100 - percent_containing_water
calories = calories_one_gr_food * percent_food

print(f"{calories:.4f}")