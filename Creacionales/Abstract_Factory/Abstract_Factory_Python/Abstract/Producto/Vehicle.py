from abc import ABC, abstractmethod

# Abstract Product: Vehículo
class Vehicle(ABC):
    @abstractmethod
    def assemble(self, engine, wheel, light):
        pass