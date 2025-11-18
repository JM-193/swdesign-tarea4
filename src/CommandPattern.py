from abc import ABC, abstractmethod
from typing import List, Tuple
from ObserverPattern import Customer
from DecoratorPattern import MenuItem

# ============================================================================
# COMMAND PATTERN - To encapsulate orders
# ============================================================================

class Command(ABC):
    """Interface for commands"""

    @abstractmethod
    def execute(self) -> None:
        """Executes the command"""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Returns command description"""
        pass


class OrderCommand(Command):
    """Command to place an order"""

    def __init__(self, customer: Customer, item: MenuItem, item_type: str):
        self._customer = customer
        self._item = item
        self._item_type = item_type  # 'beverage' or 'food'

    def execute(self) -> None:
        """Displays the customer's order"""
        print(f"Orders a {self.get_description()}")

    def get_description(self) -> str:
        return self._item.get_description()

    def get_item(self) -> MenuItem:
        return self._item

    def get_customer(self) -> Customer:
        return self._customer

    def get_item_type(self) -> str:
        return self._item_type


class PrepareCommand(Command):
    """Command to prepare an item"""

    def __init__(self, worker: str, item_type: str, description: str):
        self._worker = worker
        self._item_type = item_type
        self._description = description

    def execute(self) -> None:
        """Prepares the item"""
        print(f"[{self._worker}]: Preparing {self._item_type}: {self._description}")

    def get_description(self) -> str:
        return self._description
