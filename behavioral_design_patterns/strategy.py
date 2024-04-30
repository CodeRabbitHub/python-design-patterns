from abc import ABC, abstractmethod


# Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


# Concrete strategies
class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b


class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b


class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b


# Context
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)


# Client code
if __name__ == "__main__":
    # Client chooses a strategy
    add_strategy = AddStrategy()
    subtract_strategy = SubtractStrategy()
    multiply_strategy = MultiplyStrategy()

    # Client creates a context with the chosen strategy
    context = Context(add_strategy)
    result = context.execute_strategy(5, 3)
    print("Result of addition:", result)  # Output: Result of addition: 8

    # Client changes the strategy at runtime
    context = Context(subtract_strategy)
    result = context.execute_strategy(5, 3)
    print("Result of subtraction:", result)  # Output: Result of subtraction: 2

    context = Context(multiply_strategy)
    result = context.execute_strategy(5, 3)
    print("Result of multiplication:", result)  # Output: Result of multiplication: 15
