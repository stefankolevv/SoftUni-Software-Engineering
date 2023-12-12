class Clothes:
    def __init__(self, type_of_garment, price):
        self.type_of_garment = type_of_garment
        self.price = price

    def get_info(self):
        return f"Thank you! \nSummary: You ordered \'{self.type_of_garment}\' for the price of \'{self.price}\'"

order_summary = []
order = input()
type_of_garment, price = order.split(', ')
order_info = Clothes(type_of_garment, price)
order_summary.append(order_info)

clothes_list = ['trousers', 'dress', 'shirt', 't-shirt', 'tank top', 'shorts']

for current_order in order_summary:
    if type_of_garment not in clothes_list:
        print(f'Error! This type of garment {type_of_garment} is not in our clothes list. That\'s what we have got:')
        print(', '.join(clothes_list))
    else:
        print(current_order.get_info())
