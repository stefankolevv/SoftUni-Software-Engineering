def multiplication_sign(num1, num2, num3):
    multiplication_result = num1 * num2 * num3
    if multiplication_result > 0:
        print("positive")
    else:
        print("negative")

num1 = int(input())
num2 = int(input())
num3 = int(input())
result = multiplication_sign(num1, num2, num3)
