# Component interface
class Coffee:
    def cost(self):
        """
        Calculate the cost of the coffee.

        Returns:
            float: The cost of the coffee.
        """
        pass

    def description(self):
        """
        Get the description of the coffee.

        Returns:
            str: The description of the coffee.
        """
        pass


# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 2

    def description(self):
        return "Simple Coffee"


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ", Sugar"


# Example usage
coffee = SimpleCoffee()
print("Cost:", coffee.cost(), "Description:", coffee.description())

# Adding decorators
coffee_with_milk = MilkDecorator(coffee)
print("Cost:", coffee_with_milk.cost(), "Description:", coffee_with_milk.description())

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(
    "Cost:",
    coffee_with_milk_and_sugar.cost(),
    "Description:",
    coffee_with_milk_and_sugar.description(),
)
