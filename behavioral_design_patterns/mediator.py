from abc import ABC, abstractmethod


# Mediator interface
class Mediator(ABC):
    @abstractmethod
    def send_message(self, sender: object, message: str):
        pass


# Concrete mediator
class ChatRoom(Mediator):
    def send_message(self, sender: object, message: str):
        print(f"[{sender.name}]: {message}")


# Colleague base class
class Colleague:
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message: str):
        self.mediator.send_message(self, message)


# Concrete colleague
class User(Colleague):
    def __init__(self, name: str, mediator: Mediator):
        super().__init__(name, mediator)

    def send_message(self, message: str):
        self.send(message)


# Client code
if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)

    user1.send_message("Hi, Bob!")
    user2.send_message("Hi, Alice!")
