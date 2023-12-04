def is_valid_command(command):
    return command.isalpha() and command[0].isupper()


def is_valid_string(message):
    if message.count(":") == 1 and "[" in message and "]" in message:
        start_bracket = message.index("[")
        end_bracket = message.index("]")
        content = message[start_bracket + 1:end_bracket]
        return len(content) >= 8 and content.isalpha()
    return False


def translate_message(command, content):
    numbers = [str(ord(char)) for char in content]
    return f"{command}: {' '.join(numbers)}"


def process_input():
    n = int(input())
    for _ in range(n):
        message = input().strip()
        command_start = message.find("!")
        command_end = message.find(":")

        if command_start != -1 and command_end != -1:
            command = message[command_start + 1:command_end].strip()
            content_start = message.find("[")
            content_end = message.find("]", command_end)

            if is_valid_command(command) and is_valid_string(message[content_start:content_end + 1]):
                content = message[content_start + 1:content_end]
                print(translate_message(command, content))
            else:
                print("The message is invalid")
        else:
            print("The message is invalid")


if __name__ == "__main__":
    process_input()
