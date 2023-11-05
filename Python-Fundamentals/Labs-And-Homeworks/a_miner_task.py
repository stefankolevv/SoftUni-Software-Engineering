resources = {}
while True:
    current_resources = input()
    if current_resources == "stop":
        break
    current_quantity = int(input())
    if current_resources not in resources.keys(): #if current_resources not in resources
        resources[current_resources] = 0
    resources[current_resources] += current_quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
