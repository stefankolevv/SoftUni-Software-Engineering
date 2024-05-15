import re

def process_line(line):
    line = line.strip()
    line = re.sub(r'[-,.\!?]', '@', line)
    words = line.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

def even_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for index, line in enumerate(lines):
            if index % 2 == 0:
                processed_line = process_line(line)
                print(processed_line)

even_lines('files/text.txt')