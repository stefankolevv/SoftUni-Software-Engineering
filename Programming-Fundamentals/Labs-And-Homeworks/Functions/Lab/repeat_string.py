repeat_string = lambda string, n: string * n

string = input()
counter = int(input())
result = repeat_string(string, counter)
print(result)