single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ":":
        print(f":{single_string[index+1]}")
