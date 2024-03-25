import os

def directory_traversal():
    directory_path = input('Enter a directory path: ')

    files_by_extension = {}

    with open('files/report.txt', 'w') as report:
        for root, _, files in os.walk(directory_path):
            for file in files:
                _, extension = os.path.splitext(file)

                if extension:
                    extension = extension[1:]

                    if extension not in files_by_extension:
                        files_by_extension[extension] = []

                    files_by_extension[extension].append(file)

        for extension in sorted(files_by_extension.keys()):
            report.write(f'.{extension}\n')
            for file in sorted(files_by_extension[extension]):
                report.write(f'- - - {file}\n')

directory_traversal()