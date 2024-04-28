class MonostateSingleton:
    _shared_state = {"value": None}

    def __init__(self, value):
        self.__dict__ = self._shared_state
        if self.value is None:  # Check if value is not set yet
            self.value = value


# Example usage:
instance1 = MonostateSingleton(10)
print("Instance 1 value:", instance1.value)  # Output: 10

instance2 = MonostateSingleton(20)
print("Instance 2 value:", instance2.value)  # Output: 20

# Both instances share the same state
print("Instance 1 value:", instance1.value)  # Output: 20
print("Instance 2 value:", instance2.value)  # Output: 20
