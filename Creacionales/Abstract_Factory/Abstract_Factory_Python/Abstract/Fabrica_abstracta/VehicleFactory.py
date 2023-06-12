from abc import ABC, abstractmethod

# Abstract Factory: Fabrica de Vehículos
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_wheel(self):
        pass

    @abstractmethod
    def create_light(self):
        pass