def sorting_cheeses(**kwargs):
    result = ''
    sorted_result = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )
    for cheese_name, quantities in sorted_result:
        result += cheese_name + '\n'
        for quantity in sorted(quantities, reverse=True):
            result += f'{quantity}\n'
    return result