class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value):
        self.value = value


# Example usage:
obj1 = Singleton(1)
obj2 = Singleton(2)

print(obj1 is obj2)  # Output: True
print(obj1.value)  # Output: 1
print(obj2.value)  # Output: 1
