class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
print("Object created", s1)
s2 = Singleton()
print("Object created", s2)
