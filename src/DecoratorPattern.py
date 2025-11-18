from abc import ABC, abstractmethod
from typing import List


# ============================================================================
# DECORATOR PATTERN - To customize beverages and food items
# ============================================================================

class MenuItem(ABC):
    """Base component for menu items"""

    @abstractmethod
    def get_description(self) -> str:
        """Returns the description of the item"""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Returns the price of the item"""
        pass


class Beverage(MenuItem):
    """Base beverage"""

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_description(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price


class Food(MenuItem):
    """Base food item"""

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_description(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price


class MenuItemDecorator(MenuItem):
    """Base decorator to add extras to items"""

    def __init__(self, menu_item: MenuItem):
        self._menu_item = menu_item

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    def _add_extra(self, description: str, extra: str) -> str:
        """Smartly adds an extra to the description"""
        if " and " in description:
            # Replace last "and" with comma, then add new extra with "and"
            last_and_index = description.rfind(" and ")
            description = description[:last_and_index] + "," + description[last_and_index + 4:]
            return f"{description} and {extra}"
        elif " with " in description:
            # Replace "with" with "and"
            return f"{description} and {extra}"
        else:
            # First extra, use "with"
            return f"{description} with {extra}"


class MilkDecorator(MenuItemDecorator):
    """Decorator to add milk"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return self._add_extra(base, "milk")

    def get_price(self) -> float:
        return self._menu_item.get_price() + 0.5


class CreamDecorator(MenuItemDecorator):
    """Decorator to add cream"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return self._add_extra(base, "cream")

    def get_price(self) -> float:
        return self._menu_item.get_price() + 0.6


class DoubleEspressoDecorator(MenuItemDecorator):
    """Decorator to make double espresso coffee"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return f"Double espresso {base.lower()}"

    def get_price(self) -> float:
        return self._menu_item.get_price() + 1.5


class CinnamonDecorator(MenuItemDecorator):
    """Decorator to add cinnamon"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return self._add_extra(base, "cinnamon")

    def get_price(self) -> float:
        return self._menu_item.get_price() + 0.3


class ChocolateFillingDecorator(MenuItemDecorator):
    """Decorator to add chocolate filling"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return self._add_extra(base, "chocolate filling")

    def get_price(self) -> float:
        return self._menu_item.get_price() + 1.0


class HamCheeseFillingDecorator(MenuItemDecorator):
    """Decorator to add ham and cheese filling"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return self._add_extra(base, "ham and cheese filling")

    def get_price(self) -> float:
        return self._menu_item.get_price() + 1.2

class CaramelToppingDecorator(MenuItemDecorator):
    """Decorator to add caramel topping"""

    def get_description(self) -> str:
        base = self._menu_item.get_description()
        return self._add_extra(base, "caramel topping")

    def get_price(self) -> float:
        return self._menu_item.get_price() + 0.8
