from abc import ABC, abstractmethod


# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass


# Concrete Visitor implementing the Visitor interface
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        print(
            f"ConcreteVisitor: Visiting ConcreteElementA with {element.operation_a()}"
        )

    def visit_concrete_element_b(self, element):
        print(
            f"ConcreteVisitor: Visiting ConcreteElementB with {element.operation_b()}"
        )


# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Elements implementing the Element interface
class ConcreteElementA(Element):
    def operation_a(self):
        return "operation A"

    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(Element):
    def operation_b(self):
        return "operation B"

    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)


# Object structure
class ObjectStructure:
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)


# Client code
if __name__ == "__main__":
    visitor = ConcreteVisitor()

    object_structure = ObjectStructure()
    object_structure.attach(ConcreteElementA())
    object_structure.attach(ConcreteElementB())

    object_structure.accept(visitor)
