from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Receiver
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            self.commands[slot].execute()
        else:
            print("No command set for this button")


# Client
if __name__ == "__main__":
    # Create receiver
    light = Light()

    # Create command objects
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Create invoker
    remote_control = RemoteControl()

    # Set commands for slots on remote control
    remote_control.set_command(0, light_on)
    remote_control.set_command(1, light_off)

    # Press buttons on remote control
    remote_control.press_button(0)  # Output: Light is on
    remote_control.press_button(1)  # Output: Light is off
    remote_control.press_button(2)  # Output: No command set for this button
