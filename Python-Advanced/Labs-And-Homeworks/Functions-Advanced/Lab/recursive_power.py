def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power-1)
