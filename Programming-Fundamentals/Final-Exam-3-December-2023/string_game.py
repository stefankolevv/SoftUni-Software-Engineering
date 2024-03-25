def string_game(input_string, commands):
    for command in commands:
        tokens = command.split()
        action = tokens[0]

        if action == "Change":
            character, replacement = tokens[1], tokens[2]
            input_string = input_string.replace(character, replacement)
            print(input_string)
        elif action == "Includes":
            substring = tokens[1]
            print(str(substring in input_string))
        elif action == "End":
            substring = tokens[1]
            print(str(input_string.endswith(substring)))
        elif action == "Uppercase":
            input_string = input_string.upper()
            print(input_string)
        elif action == "FindIndex":
            character = tokens[1]
            index = input_string.find(character)
            print(index)
        elif action == "Cut":
            start_index, count = int(tokens[1]), int(tokens[2])
            cut_characters = input_string[start_index:start_index + count]
            print(cut_characters)

initial_string = input()
commands = []
while True:
    command = input()
    if command == "Done":
        break
    commands.append(command)

string_game(initial_string, commands)
