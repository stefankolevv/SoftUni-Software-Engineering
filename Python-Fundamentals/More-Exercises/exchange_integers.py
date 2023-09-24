num_1 = int(input())
num_2 = int(input())

print("Before:")
print(f"a = {num_1}")
print(f"b = {num_2}")

temp = num_1
num_1 = num_2
num_2 = temp

print("After:")
print(f"a = {num_1}")
print(f"b = {num_2}")
