from abc import ABC, abstractmethod


# Define abstract product interfaces
class Chair(ABC):
    def __init__(self, material="Unknown"):
        self.material = material

    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    def __init__(self, length=0):
        self.length = length

    @abstractmethod
    def lie_on(self):
        pass


# Define concrete product classes
class ModernChair(Chair):
    def __init__(self, material="Plastic", legs=4):
        super().__init__(material)
        self.legs = legs

    def sit_on(self):
        return f"Sitting on a modern chair with {self.legs} legs"


class VintageChair(Chair):
    def __init__(self, material="Wood", armrests="Wooden"):
        super().__init__(material)
        self.armrests = armrests

    def sit_on(self):
        return f"Sitting on a vintage chair with {self.armrests} armrests"


class ModernSofa(Sofa):
    def __init__(self, length=80, color="Gray"):
        super().__init__(length)
        self.color = color

    def lie_on(self):
        return f"Lying on a modern sofa of length {self.length} in {self.color} color"


class VintageSofa(Sofa):
    def __init__(self, length=70, pattern="Floral"):
        super().__init__(length)
        self.pattern = pattern

    def lie_on(self):
        return f"Lying on a vintage sofa of length {self.length} with {self.pattern} pattern"


# Define abstract factory interface
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


# Define concrete factory classes
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self, material="Plastic", legs=4):
        return ModernChair(material, legs)

    def create_sofa(self, length=80, color="Gray"):
        return ModernSofa(length, color)


class VintageFurnitureFactory(FurnitureFactory):
    def create_chair(self, material="Wood", armrests="Wooden"):
        return VintageChair(material, armrests)

    def create_sofa(self, length=70, pattern="Floral"):
        return VintageSofa(length, pattern)


# Client code
if __name__ == "__main__":
    modern_factory = ModernFurnitureFactory()
    modern_chair = modern_factory.create_chair()
    modern_sofa = modern_factory.create_sofa()

    print(modern_chair.sit_on())  # Output: Sitting on a modern chair with 4 legs
    print(
        modern_sofa.lie_on()
    )  # Output: Lying on a modern sofa of length 80 in Gray color

    vintage_factory = VintageFurnitureFactory()
    vintage_chair = vintage_factory.create_chair()
    vintage_sofa = vintage_factory.create_sofa()

    print(
        vintage_chair.sit_on()
    )  # Output: Sitting on a vintage chair with wooden armrests
    print(
        vintage_sofa.lie_on()
    )  # Output: Lying on a vintage sofa of length 70 with floral pattern
