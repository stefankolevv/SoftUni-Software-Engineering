def process_data(data_type, value):
    if data_type == "int":
        result = int(value) * 2
    elif data_type == "real":
        result = "{:.2f}".format(float(value) * 1.5)
    elif data_type == "string":
        result = "$" + value + "$"

    return result

data_type = input()
value = input()
output = process_data(data_type, value)
print(output)
