import os


def create_file(file_name):
    with open(f'files/{file_name}', 'w') as file:
        pass


def add_content(file_name, content):
    with open(f'files/{file_name}', 'a') as file:
        file.write(content + '\n')


def replace_string(file_name, old_string, new_string):
    try:
        with open(f'files/{file_name}', 'r') as file:
            file_content = file.read()

        new_content = file_content.replace(old_string, new_string)

        with open(f'files/{file_name}', 'w') as file:
            file.write(new_content)
    except FileNotFoundError:
        print('An error occurred')


def delete_file(file_name):
    try:
        os.remove(f'files/{file_name}')
    except FileNotFoundError:
        print('An error occurred')


def file_manipulator():
    while True:
        command = input()
        if command == 'End':
            break

        parts = command.split('-')
        action = parts[0]
        file_name = parts[1]

        if action == 'Create':
            create_file(file_name)
        elif action == 'Add':
            content = parts[2]
            add_content(file_name, content)
        elif action == 'Replace':
            old_string = parts[2]
            new_string = parts[3]
            replace_string(file_name, old_string, new_string)
        elif action == 'Delete':
            delete_file(file_name)


file_manipulator()