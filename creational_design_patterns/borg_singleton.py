class Borg:
    _shared_state = {}  # Class attribute to store shared state

    def __init__(self):
        self.__dict__ = (
            self._shared_state
        )  # Make instance attributes point to the shared state

    def __str__(self):
        return str(self._shared_state)


# Example usage
b1 = Borg()
b1.x = 10

b2 = Borg()
print(b2)  # Output: {'x': 10}

b2.y = 20

print(b1)  # Output: {'x': 10, 'y': 20}
