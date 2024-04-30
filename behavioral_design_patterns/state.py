from abc import ABC, abstractmethod


# Context
class Context:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def request(self):
        if self._state:
            self._state.handle()
        else:
            print("No state set.")


# State interface
class State(ABC):
    @abstractmethod
    def handle(self):
        pass


# Concrete states
class ConcreteStateA(State):
    def handle(self):
        print("Handling request in state A.")


class ConcreteStateB(State):
    def handle(self):
        print("Handling request in state B.")


# Client code
if __name__ == "__main__":
    context = Context()

    # Set initial state
    state_a = ConcreteStateA()
    context.set_state(state_a)
    context.request()  # Output: Handling request in state A.

    # Change state
    state_b = ConcreteStateB()
    context.set_state(state_b)
    context.request()  # Output: Handling request in state B.
