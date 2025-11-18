from abc import ABC, abstractmethod
from typing import List
from DecoratorPattern import Beverage, Food, MilkDecorator, \
    CreamDecorator, DoubleEspressoDecorator, CinnamonDecorator, \
    ChocolateFillingDecorator, HamCheeseFillingDecorator, CaramelToppingDecorator
from ObserverPattern import Customer, OrderSystem
from CommandPattern import OrderCommand, PrepareCommand
from Worker import Barista, Baker


# ============================================================================
# MAIN SIMULATION
# ============================================================================

def print_customer_header(customer: Customer):
    """Prints the header for a customer"""
    print(f"\nCustomer: {customer.get_name()}")

def main():
    """Main function that executes the simulation"""
    print("\n=== Coffee Shop Simulation ===")

    # Create order system
    order_system = OrderSystem()

    # Create customers
    juan = Customer("Juan")
    mary = Customer("Mary")

    # Register customers in the system
    order_system.attach(juan)
    order_system.attach(mary)

    # Create workers
    barista = Barista()
    baker = Baker()

    # List to store order commands
    order_commands: List[OrderCommand] = []

    # Customer Juan
    print_customer_header(juan)

    # Juan orders a coffee with milk and cinnamon
    coffee_juan = Beverage("Coffee", 2.5)
    coffee_juan = MilkDecorator(coffee_juan)
    coffee_juan = CreamDecorator(coffee_juan)
    coffee_juan = CinnamonDecorator(coffee_juan)
    order_cmd_1 = OrderCommand(juan, coffee_juan, "beverage")
    order_commands.append(order_cmd_1)
    order_cmd_1.execute()

    # Juan orders a muffin with chocolate filling
    muffin_juan = Food("Muffin", 3.0)
    muffin_juan = ChocolateFillingDecorator(muffin_juan)
    muffin_juan = CaramelToppingDecorator(muffin_juan)
    order_cmd_2 = OrderCommand(juan, muffin_juan, "food")
    order_commands.append(order_cmd_2)
    order_cmd_2.execute()

    # Customer Mary
    print_customer_header(mary)

    # Mary orders a green tea
    tea_mary = Beverage("Green tea", 2.0)
    order_cmd_3 = OrderCommand(mary, tea_mary, "beverage")
    order_commands.append(order_cmd_3)
    order_cmd_3.execute()

    # Mary orders a double espresso coffee with cream
    coffee_mary = Beverage("Coffee", 2.5)
    coffee_mary = DoubleEspressoDecorator(coffee_mary)
    coffee_mary = CreamDecorator(coffee_mary)
    order_cmd_4 = OrderCommand(mary, coffee_mary, "beverage")
    order_commands.append(order_cmd_4)
    order_cmd_4.execute()

    # Mary orders a ham and cheese sandwich
    sandwich_mary = Food("Sandwich", 4.0)
    sandwich_mary = HamCheeseFillingDecorator(sandwich_mary)
    order_cmd_5 = OrderCommand(mary, sandwich_mary, "food")
    order_commands.append(order_cmd_5)
    order_cmd_5.execute()

    # Prepare the orders
    print ("\n")
    for order_cmd in order_commands:
        if order_cmd.get_item_type() == "beverage":
            barista.prepare(order_cmd.get_item(), order_cmd.get_item_type()).execute()
        else:
            baker.prepare(order_cmd.get_item(), order_cmd.get_item_type()).execute()

    # Notify customers
    order_system.notify_all_ready()


if __name__ == "__main__":
    main()
