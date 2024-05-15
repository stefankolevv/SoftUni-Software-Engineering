from typing import List

from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.base_client import BaseClient
from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient

class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in {"FullTimeWaiter", "HalfTimeWaiter"}:
            return f"{waiter_type} is not a recognized waiter type."
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return f"{waiter_name} is already on the staff."
        if waiter_type == "FullTimeWaiter":
            waiter = FullTimeWaiter(waiter_name, hours_worked)
        else:
            waiter = HalfTimeWaiter(waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in {"RegularClient", "VIPClient"}:
            return f"{client_type} is not a recognized client type."
        for client in self.clients:
            if client.name == client_name:
                return f"{client_name} is already a client."
        if client_type == "RegularClient":
            client = RegularClient(client_name)
        else:
            client = VIPClient(client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return waiter.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        for client in self.clients:
            if client.name == client_name:
                points_earned = client.earning_points(order_amount)
                return f"{client_name} earned {points_earned} points from the order."
        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        for client in self.clients:
            if client.name == client_name:
                discount_percentage, remaining_points = client.apply_discount()
                return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        return f"{client_name} cannot get a discount because this client is not admitted!"

    def apply_discount(self):
        for client in self.clients:
            if client.name == client_name:
                discount_percentage, remaining_points = client.apply_discount()
                return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)
        waiter_details = "\n".join(
            str(waiter) for waiter in sorted(self.waiters, key=lambda x: x.calculate_earnings(), reverse=True))
        return f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\nTotal Clients Unused Points: {total_client_points}\nTotal Clients Count: {clients_count}\n** Waiter Details **\n{waiter_details}"
