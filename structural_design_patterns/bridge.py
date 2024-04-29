# Abstraction interface
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        self.device.toggle_power()

    def volume_up(self):
        self.device.volume_up()

    def volume_down(self):
        self.device.volume_down()


# Implementor interface
class Device:
    def toggle_power(self):
        """
        Toggle the power of the device.
        """
        pass

    def volume_up(self):
        """
        Increase the volume of the device.
        """
        pass

    def volume_down(self):
        """
        Decrease the volume of the device.
        """
        pass


# Concrete Implementor 1: TV
class TV(Device):
    def __init__(self):
        self.power_on = False
        self.volume = 5

    def toggle_power(self):
        self.power_on = not self.power_on
        if self.power_on:
            print("TV turned ON")
        else:
            print("TV turned OFF")

    def volume_up(self):
        if self.power_on:
            self.volume += 1
            print(f"Volume increased to {self.volume}")

    def volume_down(self):
        if self.power_on:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")


# Concrete Implementor 2: Radio
class Radio(Device):
    def __init__(self):
        self.power_on = False
        self.volume = 3

    def toggle_power(self):
        self.power_on = not self.power_on
        if self.power_on:
            print("Radio turned ON")
        else:
            print("Radio turned OFF")

    def volume_up(self):
        if self.power_on:
            self.volume += 1
            print(f"Volume increased to {self.volume}")

    def volume_down(self):
        if self.power_on:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")


# Example usage
tv = TV()
radio = Radio()

tv_remote = RemoteControl(tv)
radio_remote = RemoteControl(radio)

# Turning on TV and adjusting volume
tv_remote.toggle_power()  # Output: TV turned ON
tv_remote.volume_up()  # Output: Volume increased to 6

# Turning on Radio and adjusting volume
radio_remote.toggle_power()  # Output: Radio turned ON
radio_remote.volume_down()  # Output: Volume decreased to 2
