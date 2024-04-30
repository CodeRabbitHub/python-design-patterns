# Subject (Observable) class
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Observer interface
class Observer:
    def update(self, message):
        pass


# Concrete Observer classes
class ConcreteObserverA(Observer):
    def update(self, message):
        print("ConcreteObserverA received:", message)


class ConcreteObserverB(Observer):
    def update(self, message):
        print("ConcreteObserverB received:", message)


# Client code
if __name__ == "__main__":
    # Create subject
    subject = Subject()

    # Create observers
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    # Attach observers to subject
    subject.attach(observer_a)
    subject.attach(observer_b)

    # Notify observers
    subject.notify("Hello observers!")
