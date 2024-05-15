from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '' or value.strip() == ' ':
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value.strip() not in {'Regular', 'VIP'}:
            # From value.strip not == 'Regular' / not == 'VIP' to {'Regular, VIP'} because of errors while running
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        if self.points >= 100:
            discount_percentage = 10
            used_points = 100
        elif 50 <= self.points < 100:
            discount_percentage = 5
            used_points = 50
        else:
            discount_percentage = 0
            used_points = 0
        self.points -= used_points
        return discount_percentage, self.points