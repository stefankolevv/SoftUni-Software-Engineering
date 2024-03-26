from abc import ABC, abstractmethod

class Resturant:
    @abstractmethod
    def menu(self):
        pass

    def order(self):
        pass

    def bill(self):
        pass