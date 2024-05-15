from project.clients.base_client import BaseClient
import math

class VIPClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: float):
        return int(order_amount / 5)