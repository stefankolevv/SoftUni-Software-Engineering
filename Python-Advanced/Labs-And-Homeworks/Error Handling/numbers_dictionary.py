numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"\nThe variable number must be an integer\n{numbers_dictionary}")

    line = input()

line = input()

while line != "Remove":
    searched = line

    try:
        print(f'\n{numbers_dictionary[searched]}')
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    searched = line

    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in dictionary\n{numbers_dictionary}")

    line = input()