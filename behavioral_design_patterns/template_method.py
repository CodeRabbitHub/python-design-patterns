from abc import ABC, abstractmethod


# Abstract class defining the template method
class AbstractClass(ABC):
    def template_method(self):
        self.common_operation1()
        self.custom_operation1()
        self.common_operation2()
        self.custom_operation2()

    def common_operation1(self):
        print("AbstractClass: Performing common operation 1")

    def common_operation2(self):
        print("AbstractClass: Performing common operation 2")

    @abstractmethod
    def custom_operation1(self):
        pass

    @abstractmethod
    def custom_operation2(self):
        pass


# Concrete class implementing the abstract class
class ConcreteClassA(AbstractClass):
    def custom_operation1(self):
        print("ConcreteClassA: Performing custom operation 1")

    def custom_operation2(self):
        print("ConcreteClassA: Performing custom operation 2")


# Another concrete class implementing the abstract class
class ConcreteClassB(AbstractClass):
    def custom_operation1(self):
        print("ConcreteClassB: Performing custom operation 1")

    def custom_operation2(self):
        print("ConcreteClassB: Performing custom operation 2")


# Client code
if __name__ == "__main__":
    print("Client: Using ConcreteClassA:")
    concrete_a = ConcreteClassA()
    concrete_a.template_method()

    print("\nClient: Using ConcreteClassB:")
    concrete_b = ConcreteClassB()
    concrete_b.template_method()
