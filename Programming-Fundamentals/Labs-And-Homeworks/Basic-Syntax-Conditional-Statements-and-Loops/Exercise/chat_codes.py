number_of_messages = int(input())

for current_message in range(number_of_messages):
    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    else:
        print("Bye.")