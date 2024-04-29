# Subsystem components
class CPU:
    def freeze(self):
        print("CPU: Freezing...")

    def jump(self, address):
        print(f"CPU: Jumping to address {address}")

    def execute(self):
        print("CPU: Executing...")


class Memory:
    def load(self, address, data):
        print(f"Memory: Loading data '{data}' to address {address}")


class HardDrive:
    def read(self, lba, size):
        print(f"Hard Drive: Reading {size} bytes from LBA {lba}")


# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print("Starting computer...")
        self.cpu.freeze()
        self.memory.load(0, "BOOT_ADDRESS")
        self.cpu.jump("BOOT_ADDRESS")
        self.cpu.execute()
        self.hard_drive.read(0, 1024)
        print("Computer started successfully!")


# Client code
computer_facade = ComputerFacade()
computer_facade.start()
