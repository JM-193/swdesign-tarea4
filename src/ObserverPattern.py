from abc import ABC, abstractmethod
from typing import List


# ============================================================================
# OBSERVER PATTERN - To notify customers when orders are ready
# ============================================================================

class Observer(ABC):
    """Interface for observers"""

    @abstractmethod
    def update(self, message: str) -> None:
        """Receives notifications from the subject"""
        pass


class Subject(ABC):
    """Interface for observable subjects"""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attaches an observer"""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Removes an observer"""
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """Notifies all observers"""
        pass


class Customer(Observer):
    """Customer who observes the status of their orders"""

    def __init__(self, name: str):
        self._name = name
        self._notifications: List[str] = []

    def get_name(self) -> str:
        return self._name

    def update(self, message: str) -> None:
        """Receives notification when the order is ready"""
        self._notifications.append(message)

    def get_notifications(self) -> List[str]:
        return self._notifications


class OrderSystem(Subject):
    """Order system that notifies customers"""

    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

    def notify_all_ready(self) -> None:
        """Notifies that all orders are ready"""
        print("\n[System]: Customers are notified when their orders are ready.\n")
