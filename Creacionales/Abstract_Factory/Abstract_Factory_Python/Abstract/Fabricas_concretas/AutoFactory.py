from Abstract.Fabrica_abstracta.VehicleFactory import VehicleFactory
from Abstract.Productos_concretos.Auto import Auto
from Abstract.Productos_concretos.AutoLight import AutoLight
from Abstract.Productos_concretos.Engine import Engine
from Abstract.Productos_concretos.Wheel import Wheel

# Concrete Factory: Fabrica de Autos
class AutoFactory(VehicleFactory):
    def create_vehicle(self):
        return Auto()

    def create_engine(self):
        return Engine()

    def create_wheel(self):
        return Wheel()

    def create_light(self):
        return AutoLight()