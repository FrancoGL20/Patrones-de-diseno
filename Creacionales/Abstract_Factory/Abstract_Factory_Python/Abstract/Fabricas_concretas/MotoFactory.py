from Abstract.Fabrica_abstracta.VehicleFactory import VehicleFactory
from Abstract.Productos_concretos.Moto import Moto
from Abstract.Productos_concretos.MotoLight import MotoLight
from Abstract.Productos_concretos.Engine import Engine
from Abstract.Productos_concretos.Wheel import Wheel

# Concrete Factory: Fabrica de Motos
class MotoFactory(VehicleFactory):
    def create_vehicle(self):
        return Moto()

    def create_engine(self):
        return Engine()

    def create_wheel(self):
        return Wheel()

    def create_light(self):
        return MotoLight()