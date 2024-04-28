from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, case, motherboard, cpu, ram, storage, **kwargs):
        self.case = case
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.components = kwargs

    def __str__(self):
        components_str = ", ".join(
            [f"{key}: {value}" for key, value in self.components.items()]
        )
        return f"Computer: {self.case}, {self.motherboard}, {self.cpu}, {self.ram}, {self.storage}, {components_str}"


class ComputerBuilder(ABC):
    def __init__(self, **kwargs):
        self.computer = Computer("", "", "", "", "", **kwargs)

    @abstractmethod
    def set_case(self, case):
        pass

    @abstractmethod
    def set_motherboard(self, motherboard):
        pass

    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    def set_component(self, component, value):
        self.computer.components[component] = value
        return self

    def remove_component(self, component):
        if component in self.computer.components:
            del self.computer.components[component]
        return self

    def build(self):
        return self.computer


class DesktopComputerBuilder(ComputerBuilder):
    def set_case(self, case):
        self.computer.case = case
        return self

    def set_motherboard(self, motherboard):
        self.computer.motherboard = motherboard
        return self

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self


# Client code
if __name__ == "__main__":
    desktop_builder = DesktopComputerBuilder(
        sound_card="Sound Blaster X3", wifi_card="Intel AX200"
    )
    desktop = (
        desktop_builder.set_case("Tower")
        .set_motherboard("ATX")
        .set_cpu("Intel Core i7")
        .set_ram("16GB DDR4")
        .set_storage("512GB SSD")
        .remove_component("wifi_card")
        .build()
    )

    print(desktop)
