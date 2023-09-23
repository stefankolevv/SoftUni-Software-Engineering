number_of_string = int(input())

for current_string in range(number_of_string):
    pure_or_not_pure_string = input()

    if "," in pure_or_not_pure_string or \
            "." in pure_or_not_pure_string or \
            "_" in pure_or_not_pure_string:
        print(f"{pure_or_not_pure_string} is not pure!")
    else:
        print(f"{pure_or_not_pure_string} is pure.")
