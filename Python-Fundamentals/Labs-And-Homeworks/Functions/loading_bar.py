def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = some_number // 10
    return f"{some_number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
