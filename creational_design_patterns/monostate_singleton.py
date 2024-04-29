class MonoStateSingleton:
    __shared_state = {"value": None}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Demo
s1 = MonoStateSingleton()
s2 = MonoStateSingleton()

print(s1)
print(s2)

s1.set_value(10)
print("Value from s2:", s2.get_value())  # Output: 10
