length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
total = volume / 1000
acc_volume = total * (percent / 100)
result = total - acc_volume

print(result)