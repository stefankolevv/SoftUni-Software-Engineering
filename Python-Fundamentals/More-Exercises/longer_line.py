import math

def closest_to_center(x1, y1, x2, y2):
    distance1 = math.sqrt(x1**2 + y1**2)
    distance2 = math.sqrt(x2**2 + y2**2)

    if distance1 <= distance2:
        return x1, y1, x2, y2
    else:
        return x2, y2, x1, y1

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    x1, y1, x2, y2 = closest_to_center(x1, y1, x2, y2)
    x3, y3, x4, y4 = closest_to_center(x3, y3, x4, y4)

    distance1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distance2 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)

    if distance1 >= distance2:
        return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"
    else:
        return f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)
