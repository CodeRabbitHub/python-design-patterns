class LazySingleton:
    _instance = None

    def __init__(self, value):
        self.value = value

    @classmethod
    def get_instance(cls, value):
        if cls._instance is None:
            cls._instance = cls(value)
        return cls._instance


# Example usage:
singleton1 = LazySingleton.get_instance(10)
print("Singleton 1 value:", singleton1.value)  # Output: 10

singleton2 = LazySingleton.get_instance(20)
print("Singleton 2 value:", singleton2.value)  # Output: 10 (same instance)

# Modifying singleton1's value
singleton1.value = 30

# singleton2 reflects the change made to singleton1's value
print("Singleton 2 value:", singleton2.value)  # Output: 30
