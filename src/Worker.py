from CommandPattern import PrepareCommand
from DecoratorPattern import MenuItem

# ============================================================================
# WORKERS - Prepare the orders
# ============================================================================

class Worker:
    """Base class for workers"""

    def __init__(self, title: str):
        self._title = title

    def prepare(self, item: MenuItem, item_type: str) -> PrepareCommand:
        """Creates a preparation command"""
        return PrepareCommand(self._title, item_type, item.get_description())


class Barista(Worker):
    """Barista who prepares beverages"""

    def __init__(self):
        super().__init__("Barista")


class Baker(Worker):
    """Baker who prepares food items"""

    def __init__(self):
        super().__init__("Baker")