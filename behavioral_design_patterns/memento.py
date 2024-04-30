import copy


# Memento class
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


# Originator class
class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def save_to_memento(self):
        return Memento(copy.deepcopy(self._state))

    def restore_from_memento(self, memento):
        self._state = memento.get_state()


# Caretaker class
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


# Client code
if __name__ == "__main__":
    # Create originator
    originator = Originator()

    # Create caretaker
    caretaker = Caretaker()

    # Set initial state
    originator.set_state("State1")

    # Save state to memento
    caretaker.add_memento(originator.save_to_memento())

    # Change state
    originator.set_state("State2")

    # Save state to memento
    caretaker.add_memento(originator.save_to_memento())

    # Restore state from memento
    originator.restore_from_memento(caretaker.get_memento(0))

    print("Current state:", originator._state)  # Output: State1
