import string

def process_line(line, line_number):
    letter_count = sum(1 for char in line if char.isalpha())
    punctuation_count = sum(1 for char in line if char in string.punctuation)
    processed_line = f'Line {line_number}: {line.strip()} ({letter_count})({punctuation_count})'
    return processed_line

def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

        with open(output_file, 'w') as output:
            for index, line in enumerate(lines, start=1):
                processed_line = process_line(line, index)
                output.write(processed_line + '\n')

add_line_numbers('files/text.txt', '../Python Advanced/File Handling/files/output.txt')
